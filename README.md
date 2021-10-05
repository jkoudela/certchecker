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

### Phase 2

Add logging capabilities to the application. For each request following information has to be logged to a file. The filename and path should be stored in an environment variable called CC_LOGPATH (e.g. CC_LOGPATH=/var/log/certchecker.log). In case CC_LOGPATH is empty, use the path where the application is running. All log entries are appended to the same file for the day. Each file has the following format for the name certchecker_2021_09_30.log and is created on a daily basis. The log contains the URL requested, the response code from the target and the certificate validity data. If any error occurres, report the error message with a status HTTP status code (e.g. 500,404, etc.)/or timeout in case the site is not reachable.
Introduce another environment variable CC_LOGRETENTION to introduce log rotation (delete logs older than X days). If no values is specified delete logs older than 30 days.

- **Environments variables**
  
  CC_LOGPATH - the path where logs are stored. Default is currrent directory

  CC_LOGRETENTION - the duration in days for how long the old logs are kept. Default is 30 days
