import sys
import argparse
from zipfile import ZipFile
from pathlib import Path
from subprocess import check_output
import tools

def remove_meta_inf(p_apk):
    if isinstance(p_apk, str):
        raise Exception("p_apk is not str type")

    zip = ZipFile(p_apk)
    for l in zip.namelist():
        if l.startswith('META-INF/'):
            is_signed = True
            break
    else:
        is_signed = False

    if is_signed:
        unsinged_apk_path = str(p_apk.resolve())[:-4] + "-unsigned.apk"
        zout = ZipFile(unsinged_apk_path, 'w')
        for item in zip.infolist():
            buffer = zip.read(item.filename)
            if not item.filename.startswith('META-INF/'):
                zout.writestr(item, buffer)
        zout.close()
        zip.close()
        return Path(unsinged_apk_path)
                
    return p_apk

def apksign(p_apk, key_path: str,  ks_pass: str, zip_align: str):
    try:
        if zip_align:
            signed_apk_name = p_apk.name.replace("-zipaligned.apk", "-signed.apk")
        else:
            signed_apk_name = p_apk.name.replace("-unsigned.apk", "-signed.apk")
        psigned_apk = p_apk.parent.joinpath(signed_apk_name)

        key_cmd = ['--ks', key_path,  '--ks-pass', 'pass:{}'.format(ks_pass)]
        cmd = [tools.apksigner, 'sign'] + key_cmd + ['--out', str(psigned_apk.resolve()), str(p_apk.resolve())]
        r = check_output(cmd)
    except Exception as e:
        print("apk signing error: " + str(e))
        return False

    return psigned_apk 

def validate_sign(p_apk: str):
    key_cmd = ['--print-certs', '-v', p_apk]
    cmd = [tools.apksigner, 'verify'] + key_cmd
    r = check_output(cmd)
    print(r)

def zipalign(p_apk):
    try:
        zipaligned_apk_name = p_apk.name.replace("-unsigned.apk", "")
        if zipaligned_apk_name.endswith(".apk"):
            zipaligned_apk_name = zipaligned_apk_name[:-4]
        
        zipaligned_apk_name = zipaligned_apk_name + "-zipaligned.apk"
        p_zipaligned_apk = p_apk.parent.joinpath(zipaligned_apk_name)
        if p_zipaligned_apk.exists():
            p_zipaligned_apk.unlink()
        cmd = [tools.zipalign, '-v', '-p', '4', str(p_apk.resolve()), str(p_zipaligned_apk.resolve())]
        r = check_output(cmd)
    except Exception as e:
        print("apk zipalign error: " + str(e))
        return False
    return p_zipaligned_apk
        
def main(file_path: str,key_1_path: str, key_1_alias: str, key_1_pass: str, zip_align: bool, next_signer: bool, key_2_path: str, key_2_alias: str, key_2_pass: str):
    p_apk = Path(file_path)
    if not p_apk.exists():
        raise Exception("File not founded: " + str(p_apk.resolve()))
    p_unsigned_apk = remove_meta_inf(p_apk)
    if zip_align:
        p_signed_apk = zipalign(p_unsigned_apk)
        p_zip_align_apk = p_signed_apk
    else:
        p_signed_apk  = p_unsigned_apk
    
    if p_signed_apk:
        
        p_signed_apk = apksign(p_signed_apk, key_1_path, key_1_pass,zip_align)
        if p_signed_apk:
            p_unsigned_apk.unlink()
            if zip_align:
                p_zip_align_apk.unlink()
                
            apk = str(p_signed_apk.resolve())
            validate_sign(apk)
            print(apk)
            return apk
     
if __name__ == '__main__':
  try:
    parser = argparse.ArgumentParser(
      prog = 'apk-signer',
      description = 'Sign APK',
      epilog = 'Author: Productivity Mobile CI/CD'
    )
    parser.add_argument("-f", "--file_path", help="APK/AAB path to sign", type=str, required=True)
    parser.add_argument("-k", "--key_1_path", help="Key 1 path", type=str, required=True)
    parser.add_argument("-a", "--key_1_alias", help="Key 1 alias", type=str, required=False)
    parser.add_argument("-p", "--key_1_pass", help="Key 1 pass", type=str, required=True)
    parser.add_argument("-z", "--zip_align", help="Zip align version", type=bool, required=False,default=False)
    parser.add_argument("-n", "--next_signer", help="Allow second signers", type=bool, required=False,default=False)
    parser.add_argument("-k2", "--key_2_path", help="Key 2 path", type=str, required=False)
    parser.add_argument("-a2", "--key_2_alias", help="Key 2 alias", type=str, required=False)
    parser.add_argument("-p2", "--key_2_pass", help="Key 2 pass", type=str, required=False)

        
    args = parser.parse_args()
    main(args.file_path,args.key_1_path, args.key_1_alias,args.key_1_pass,args.zip_align, args.next_signer,args.key_2_path,args.key_2_alias,args.key_2_pass)
    exit()
  except Exception as e:
    message=f"Something went wrong. Please check '--help' command if needed: {e}"
    print(f'##vso[task.logissue type=error]{message}')
    exit(1)