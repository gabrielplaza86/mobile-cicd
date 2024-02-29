# Distribute app builds to testers and users via Appetize.

## Description

Upload your app to Appetize.io to stream it in browser

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
      uses: inditex/gha-mobdistribute/appetize@v1
      with:
        path: "./MyApp.zip",
        api_host: "company.appetize.io", # only needed for enterprise hosted solution
        api_token: "yourapitoken", # get it from https://appetize.io/docs#request-api-token
        public_key: "your_public_key"
```
