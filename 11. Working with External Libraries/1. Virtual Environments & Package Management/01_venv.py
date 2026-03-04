
# install: pip install moviepy
import moviepy

# v1 - package 1 (pandas)
# v2 - package 2 (numpy)
# v3 - package 3 (moviepy)
#  ".\env2\Scripts\Activate.ps1" (To activate env2)

# pip install <>: install the package globally
# different projects may different version of an package
    ## project 1: numpy - v1
    ## project 2: numpy - v2
# global package cannot have different version of same package at same time
# use virtual environment to solve above problem

# 1. install virtualenv globally: pip install virtualenv
# 2. create virtual env: python -m venv env1
# 3. Activate the env1 environment: .\env1\Scripts\Activate.ps1 
    ## deactivate the env1: deactivate

# install a few packages
# list all installed packages in env1: pip list
# show a list of required packages to run the project: pip freeze
# generate the requirements.txt file to include all required packages for using/running the package/app: pip freeze > requirements.txt
    # when others want to use this package, they can simply run: `pip install -r requirements.txt`, to have all required dependencies installed






