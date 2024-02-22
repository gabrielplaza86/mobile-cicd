fastlane documentation
----

# Installation

Make sure you have the latest version of the Xcode command line tools installed:

```sh
xcode-select --install
```

For _fastlane_ installation instructions, see [Installing _fastlane_](https://docs.fastlane.tools/#installing-fastlane)

# Available Actions

## iOS

### ios update_config_project

```sh
[bundle exec] fastlane ios update_config_project
```

Update Config Project
  Parameters:
  - target: Specify target you want to toggle the signing mech
  - build_config: Specify build_configuration you want to toggle the signing mech
  - xcodeproj: Path to your Xcode project
  - teamid: Team ID, is used when upgrading project
  - appidentifier: Application Product Bundle Identifier
  - sign_identity: Code signing identity type
  - provision_profile_name: Provisioning profile name to use for code signing

### ios set_build_number_for_app

```sh
[bundle exec] fastlane ios set_build_number_for_app
```

Set build number for app
  Accepted parameters:
  - build_number: example 20211223132514

### ios resign_ipa_file

```sh
[bundle exec] fastlane ios resign_ipa_file
```

Codesign an existing ipa file
  Accepted parameters:
  - ipa: Ipa resign path
  - signing_identity: Code signing identity type
  - provision_profiles_string: Provisioning profile name to use for code signing
  - mobile_provision_directory: MObile provision directory

----


## Android

### android deploy_appcenter

```sh
[bundle exec] fastlane android deploy_appcenter
```



### android get_app_info

```sh
[bundle exec] fastlane android get_app_info
```

Huawei App Gallery Connect Info:
  Parameters:
  - client_id: Client id (project=N/A)
  - client_secret: Client Secret key # pragma: allowlist secret
  - app_id: App identification

### android upload_to_huawei

```sh
[bundle exec] fastlane android upload_to_huawei
```

Huawei App Gallery Connect Upload:
  Parameters:
  - client_id: Client id (project=N/A)
  - client_secret: Client Secret key # pragma: allowlist secret
  - app_id: App identification
  - apk_path: Path Apk'
  - submit_for_review: False by default

----

This README.md is auto-generated and will be re-generated every time [_fastlane_](https://fastlane.tools) is run.

More information about _fastlane_ can be found on [fastlane.tools](https://fastlane.tools).

The documentation of _fastlane_ can be found on [docs.fastlane.tools](https://docs.fastlane.tools).
