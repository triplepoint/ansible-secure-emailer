# Ansible Secure Emailer [![Build Status](https://travis-ci.org/triplepoint/ansible-secure-emailer.svg?branch=master)](https://travis-ci.org/triplepoint/ansible-secure-emailer)
Allow simple emailing of systems notifications over a secure and authenticated channel.

## Requirements
None.

## Role Variables
See the [comment default variables file](defaults/main.yml).

## Dependencies
None.

## Example Playbook
    - hosts: whatever
      roles:
        - triplepoint.secure-emailer

## Role Testing
This role is tested with `molecule`, using `pipenv` to handle dependencies and the Python testing environment.

### Setting Up Your Execution Environment
``` sh
pip install pipenv
```
Note, `pip-tools` doesn't appear to play nice with `pipenv`.  You should not have `pip-tools` installed for this to work correctly.

Once you have `pipenv` installed, you can build the execution virtualenv with:
``` sh
pipenv install --ignore-pipfile
```
This will create a virtual environment with all the Python dependency packages installed.

### Running Tests
Once you have your environment configured, you can execute `molecule` with:
``` sh
pipenv run molecule test
```

### Regenerating the Lock File
You shouldn't have to do this very often, but if you change the Python package requirements using `pipenv install {some_package}` commands or by editing the `Pipfile` directly, or if you find the build dependencies have fallen out of date, you might need to regenerate the `Pipfile.lock`.
``` sh
pipenv lock
```
Be sure and check in the regenerated `Pipfile.lock` when this process is complete.

## License
MIT
