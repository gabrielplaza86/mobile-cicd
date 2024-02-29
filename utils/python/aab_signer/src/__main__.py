import sys
import argparse
from zipfile import ZipFile
from pathlib import Path
from subprocess import check_output
import tools
import shutil

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
        unsinged_apk_path = str(p_apk.resolve())[:-4] + ".aab.unsigned"
        zout = ZipFile(unsinged_apk_path, 'w')
        for item in zip.infolist():
            buffer = zip.read(item.filename)
            if not item.filename.startswith('META-INF/'):
                zout.writestr(item, buffer)
        zout.close()
        zip.close()
        return Path(unsinged_apk_path)
                
    return p_apk

def zipalign(p_aab: str,p_aab_unaligned: str):
    try:
        cmd = [tools.zipalign, '-v', '-p', '4', p_aab_unaligned, p_aab]
        r = check_output(cmd)
    except Exception as e:
        print("aab zipalign error: " + str(e))
        return False
    return p_aab


def generate_unsigned_aab(p_aab: str):
    unsinged_aab_path = str(p_aab.resolve())[:-4] + ".aab.unsigned"
    shutil.copyfile(p_aab.resolve(), unsinged_aab_path)
    return unsinged_aab_path

def generate_unaligned_aab(p_aab: str):
    unsinged_aab_path = str(p_aab)[:-4] + ".aab.unaligned"
    shutil.move(p_aab, unsinged_aab_path)
    return unsinged_aab_path


def aabsign(p_aab: str, key_path: str,  ks_pass: str, k_alias: str):
    generate_unsigned_aab(p_aab)
    try:
        unsinged_aab_path = str(p_aab.resolve())[:-4] + ".aab.unsigned"
        key_cmd = ['-keystore', key_path,  '-storepass', ks_pass, '-keypass',ks_pass, '-signedjar', p_aab]
        cmd = [tools.jarsigner] + key_cmd + [unsinged_aab_path, k_alias]
        r = check_output(cmd)
    except Exception as e:
        print("apk signing error: " + str(e))
        return False

    return p_aab 

def validate_sign(p_aab: str):
    key_cmd = ['-verify', p_aab]
    cmd = [tools.jarsigner] + key_cmd
    r = check_output(cmd)
    if "jar verified" in r.decode('utf-8'):
        print("jarsigner verification succesful")
    else:
        print("jarsigner verification unsuccesful")


def validate_zipalign(p_aab: str):
    cmd = [tools.zipalign, '-v', '-c', '4', p_aab]
    r = check_output(cmd)
    if "Verification succesful" in r.decode('utf-8'):
        print("zipalign verification succesful")
    else:
        print("zipalign verification unsuccesful")
        
def main(file_path: str,key_1_path: str, key_1_pass: str, key_1_alias: str, zip_align: str):
    p_aab = Path(file_path)
    if not p_aab.exists():
        raise Exception("File not founded: " + str(p_aab.resolve()))
   
    p_signed_aab = aabsign(p_aab, key_1_path, key_1_pass, key_1_alias)
    if p_signed_aab:
        aab = str(p_signed_aab.resolve())
        validate_sign(aab)
        if zip_align:
            aab_unaligned = generate_unaligned_aab(aab)
            aab_zipalign = zipalign(aab,aab_unaligned)
            validate_zipalign(aab_zipalign)
        return aab
     
if __name__ == '__main__':
  try:
    parser = argparse.ArgumentParser(
      prog = 'apk-signer',
      description = 'Sign APK',
      epilog = 'Author: Productivity Mobile CI/CD'
    )
    parser.add_argument("-f", "--file_path", help="APK/AAB path to sign", type=str, required=True)
    parser.add_argument("-k", "--key_1_path", help="Key 1 path", type=str, required=True)
    parser.add_argument("-p", "--key_1_pass", help="Key 1 pass", type=str, required=True)
    parser.add_argument("-a", "--key_1_alias", help="Key 1 alias", type=str, required=True)
    parser.add_argument("-z", "--zip_align", help="Zip align version", type=bool, required=False,default=False)

    args = parser.parse_args()
    main(args.file_path,args.key_1_path, args.key_1_pass, args.key_1_alias, args.zip_align)
    exit()
  except Exception as e:
    message=f"Something went wrong. Please check '--help' command if needed: {e}"
    print(f'##vso[task.logissue type=error]{message}')
    exit(1)