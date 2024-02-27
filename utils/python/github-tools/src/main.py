#!/usr/bin/python3
from github import Github
import click
import sys
import json

# Authentication is defined via github.Auth
from github import Auth

'''
task: bash@3
input:
  env:
    REPO_NAME: ''
    PAT_TOKEN: 'xx'
  inline: |
    pip install .
    python3 main.py merge ...
'''

def github_login(token):
  try:
    auth = Auth.Token(token)
    g = Github(auth=auth)
    return g
  except Exception as ex:
    click.echo("Authentication exception: {}".format(str(ex)), err=True)
    sys.exit(1)

@click.group()
@click.version_option(package_name='github-tools')
def cli():
  pass

@cli.command(name="merge", help="Command to merge two branches")
@click.option('--repo', envvar='REPO_NAME', default='example/repo', help='repo name: example/repo')
@click.option('--main', envvar='REPO_MAIN', default='main', help='Main branch')
@click.option('--branch', envvar='REPO_BRANCH', default='', help='Secondary branch to merge')
@click.option('--token', envvar='PAT_TOKEN', default='', help='Github\'s PAT Token')
def merge_branches(repo, main, branch, token):
  g = github_login(token)
  click.echo("Merging {} from {} to {} ".format(repo, branch, main))
  try:
    repository = g.get_repo(repo)
    base = repository.get_branch(main)
    head = repository.get_branch(branch)
    merge_to_master = repository.merge(main, head.commit.sha, "merge to main")
    click.echo("merged {} from {} to {} ".format(repo, branch, main))
    sys.exit(0)

  except Exception as ex:
    click.echo("Merge exception {}".format(str(ex)), err=True)
    print(str(ex))
    sys.exit(2)

@cli.command(name="call-workflow", help="Command to trigger a gh workflow")
@click.option('--workflow', envvar='WORKFLOW_NAME', default='workflow-name', help='workflow name: workflow-name')
@click.option('--repo', envvar='REPO_NAME', default='example/repo', help='repo name: example/repo')
@click.option('--branch', envvar='REPO_BRANCH', default='', help='Secondary branch to merge')
@click.option('--token', envvar='PAT_TOKEN', default='', help='Github\'s PAT Token')
@click.option('--input', envvar='WORKFLOW_INPUT', default=None, help='Github Input variables (example: "var1=123,var2=abc") ')
def call_pipeline(workflow, repo, branch, token, input):
  click.echo(f"Calling workflow {workflow} from {repo} to {branch} ")
  g = github_login(token)
  input_dict = {}
  if input is not None:
    click.echo("Converting input ...")
    pairs = input.split(',')
    input_dict = {}

    # Iterate through the pairs and split each pair on '=' to get the key and value
    for pair in pairs:
      key, value = pair.split('=')
      # Check if the value is numeric
      #if value.isnumeric():
      #  input_dict[key] = int(value)
      #else:
      input_dict[key] = value
    input_json = json.dumps(input_dict)
    click.echo(f"Input in json format: {input_json}")
  try:
    repository = g.get_repo(repo)
    if repository:
      click.echo(f"Repo found:{repository.name}")
      workflows = repository.get_workflows()
      work = None
      # Iterate through the workflows and find the one we want
      for w in workflows:
        if w.name == workflow:
          click.echo(f"Workflow found:{w.name}")
          work=w
          break

      if work:
        click.echo(f"Launching Workflow ... {work.name}")
        result = work.create_dispatch(ref=branch, inputs=input_dict)
        click.echo(f"Workflow result: {result}")
        sys.exit(0)
      else:
        click.echo(f"Workflow not found:{workflow}", err=True)
        sys.exit(1)
    else :
      click.echo(f"Repo not found:{repo}", err=True)
      sys.exit(1)

  except Exception as ex:
    click.echo("Call exception {}".format(str(ex)), err=True)
    print(str(ex))
    sys.exit(2)

if __name__ == '__main__':
    cli()