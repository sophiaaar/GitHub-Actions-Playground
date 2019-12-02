import subprocess
import sys
import argv

print("testing scripting")

#git_branch = subprocess.check_output(['git', 'branch']).strip()
print('git_branch:' + sys.argv[1])

# data = '''{
  # "source": {
    # "branchname": "master",
    # "revision": "''' + srp_revision + '''"
  # },
  # "links": {
    # "project": "/projects/78",
    # "jobDefinition": "/projects/78/revisions/''' + srp_revision + '''/job-definitions/.yamato#upm-ci-abv.yml#trunk_verification"
  # },
  # "environmentVariables": [
    # { "key": "CUSTOM_REVISION", "value": "''' + unity_revision + '''" }
# ]
# }'''