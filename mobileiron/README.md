# Mobileiron makes distributing your apps to enterprise devices.

## Description

This action has the purpose to distribute app builds to Mobileiron.

## Dependencies

This action must be used with a runner with Python 3.10.x

## Examples usage

```
name: Continuous Integration

on:
  workflow_dispatch:

permissions:
  contents: read

jobs:
  test-actions:
    name: Distribute Tests
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      id: checkout
      uses: actions/checkout@v4
  
    - name: Run Distribute Action
      id: distribute-action
      uses: inditex/gha-mobdistribute/mobileiron@v1
      with:
        app_file_path: './test.apk'
        app_file_extension: 'apk'
        build_id: '1234'
        artifact_name: 'Android'


        owner_type: "organization"
        app_name: "mob-helloworldand"
        file: "./test.apk"
```
