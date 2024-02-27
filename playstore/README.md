# Distribute app builds to testers and users via App Center.

## Description

This action has the purpose to distribute app builds to testers and users via Visual Studio App Center.

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
    name: Appcenter Tests
    runs-on: ubuntu-latest

    steps:
    - name: Checkout
      id: checkout
      uses: actions/checkout@v4
  
    - name: Run Appcenter Action
      id: appcenter-action
      uses: inditex/gha-mobdistribute/appcenter@v1
      with:
        owner_type: "organization"
        app_name: "mob-helloworldand"
        file: "./test.apk"
```
