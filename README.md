# Project - Certificate checker

## High-level description

Create an API running in a container (optionally serverless using Azure Functions) that will get the target URL certificate and returns the certificate validity.

The project will have several phases and allows slow evolution of the application while learning new concepts along the way.

- Phase 0 - environment setup
- Phase 1 - console application with basic functionality
- Phase 2 - error handling and logging
- Phase 3 - console to API
- Phase 4 - create a container for the API
- Phase 5 - deploy the API to the cloud
- Phase 6 - operational monitoring instrumentation
- Phase 7 - frontend App (SPA app) with basic functionality
- Phase 8 - create a container, deploy and connect the SPA to the API
- Phase 9 - Wrap up, improvements, and possible extensions

Source code versioning rules:
- all code has to be stored in GIT. 
- every phase has to be developed in a branch with the following convention phaseX/task-name, e.g. phase1/initial-code-structure or phase1/get-cert-info. The idea is having an idea what is being worked on and allows to work on multiple features in paralel.
- create a pull request to merge the code with the main branch

## Project Phases

### Phase 0

**Objective**

Have the development environment set up, and all the tools in place. Learn source code versioning basics with GIT.

- install the SW
- configure all SW
- clone GIT main branch
- create a branch
- add some code, commit and push
- create a pull request
- review the merge


Skills:

- IDE basics - VS Code (recommended) or IDE of your choice (Pycharm or others)
- Python basics
- Git basics


SW requirements:

- VS Code or other editor for the code development + plugins (or other depending on your IDE choice)
- git client
- github.com account


### Phase 1

Create a console application with the following inputs and outputs:

- **Inputs**

 URL of the taget website, e.g. https://opensource.com

 - **Outputs**

 The certificate validity, e.g. 15.6.2021

