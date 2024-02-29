# Distribute app builds to testers and users via Huawei.

## Description

Huawei App Gallery Connect Upload

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
      uses: inditex/gha-mobdistribute/huawei@v1
      with:
        app_id: 'com.inditex.TEST'
        apk_path: './test.apk'
```
