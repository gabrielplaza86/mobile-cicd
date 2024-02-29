# Distribute app builds to testers and users via Jfrog-Artifactory.

## Description

Upload your app to Jfrog-Artifactory

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
      uses: inditex/gha-mobdistribute/jfrog@v1
      with:
        pattern: './test*.apk'
        repo: 'test-snapshot-local'
        repo_path: 'Developments/v1/'
```
