# Distribute app builds to testers and users via Playstore.

## Description

Upload metadata, screenshots and binaries to Google Play (via supply)

## Dependencies

This action must be used with a runner with Ruby 3.x.

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
      uses: inditex/gha-mobdistribute/playstore@v1
      with:
        application_id: 'com.inditex.TEST'
        json_key: './helloworld.json'
        path: './test.apk'
```
