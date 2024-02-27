fastlane documentation
----

# Installation

Make sure you have the latest version of the Xcode command line tools installed:

```sh
xcode-select --install
```

For _fastlane_ installation instructions, see [Installing _fastlane_](https://docs.fastlane.tools/#installing-fastlane)

# Available Actions

### distribute_to_appcenter

```sh
[bundle exec] fastlane distribute_to_appcenter
```

Allows you to upload and distribute apps to your testers on App Center:
Parameters:
- api_token: appcenter token
- owner_name: appcenter account name of the owner of the app
- owner_type: organization
- app_name: appcenter app name (as seen in app URL
- file: path to android build binary

### distribute_to_appetize

```sh
[bundle exec] fastlane distribute_to_appetize
```

Upload your app to Appetize.io to stream it in browser:
Parameters:
- path: Path to zipped build on the local filesystem. Either this or url must be specified
- api_token: Appetize.io API Token
- public_key: If not provided, a new app will be created. If provided, the existing build will be overwritten	
- api_host: Appetize API host
- platform: Platform. Either ios or android
- note: Notes you wish to add to the uploaded app

### distribute_to_jfrog

```sh
[bundle exec] fastlane distribute_to_jfrog
```

Upload your app to Jfrog-Artifactory:
Parameters:
- pattern: Patter files to be uploaded to artifactory
- repo: Artifactory repo to put the file in
- repo_path: Path to deploy within the repo, including filename	
- api_host: Appetize API host
- platform: Platform. Either ios or android
- note: Notes you wish to add to the uploaded app

----


## Android

### android distribute_to_playstore

```sh
[bundle exec] fastlane android distribute_to_playstore
```

uploads app metadata, screenshots, binaries, and app bundles to Google Play:
  Parameters:
  - application_id: package name of the application to use
  - json_key: path to a file containing service account JSON, used to authenticate with Google
  - path: Path to zipped build on the local filesystem. Either this or url must be specified
  - track_deploy: The track of the application to use

### android get_app_info

```sh
[bundle exec] fastlane android get_app_info
```

Huawei App Gallery Connect Info:
  Parameters:
  - client_id: Client id (project=N/A)
  - client_secret: Client Secret key # pragma: allowlist secret
  - app_id: App identification

### android distribute_to_huawei

```sh
[bundle exec] fastlane android distribute_to_huawei
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
