# TEST REPOSITORY
## BRANCHES
### - GITHUB_ACTIONS
- The path for running the jobs of the yml file using GitHub Actions
> root/.github/workflows/helloworld.yml
- Contents of the 'helloworld.yml' file
'''
on: #Specifies the event that will trigger the workflow
  push: #The workflow will be triggered when a push is made to the repo
    branches: #Defines on which branches the workflow will be triggered
      - main #In this case, the main branch

jobs: #Defines the jobs that will be executed
  print_hello: #Name of the first job
    runs-on: ubuntu-latest #Specifies the VM on which the task will run
    steps: #Defines the steps the job will execute
      - run: echo "Hello world!" #The specific job: display "Hello world!" on the screen

  #Example of another job similar to the previous one
  print_name:
    runs-on: ubuntu-latest
    steps:
      - run: echo "David"
      - run: echo "Closing"
'''
### - PYTEST_API
- Python file with instructions to test the API at the URL todo.pixegami.io
- Integrated Pytest for running tests
- Explained line by line

### - PYTEST_FASTAPI_CRUD
- Same as PYTEST_FASTAPI but implementing CRUD operations for users

### - PYTEST_FASTAPI
- Same as PYTEST_API but using FastAPI

### - PYTEST
- A main.py class and a test_main.py class with operations
- The test_main.py class tests some integers as parameters for the test, where one of them will cause an error during the test
- Serves as a test to understand how pytest works
