# python-typing

Experimenting with defining and validating types in Python.

This repo sets some simple tasks to help you experiment and get started using function annotations (PEP 3107) and the typing module (PEP 0484).

## Setup

Ensure you have Python 3.5 installed, then create a virtual environment targeting your installation of Python 3.5

    virtualenv pytypes --python=/usr/local/bin/python3.5
    source pytypes/bin/activate

Then install the required libraries (note that mypy-lang is installed from source so it is compatible with Python 3.5).

    `pip install -r requirements.txt'

Then you can test mypy is working by running `make type-check`.

## Tasks for completion

In greetings.py and pyblogs.py, you'll find some tasks for you to complete. These simple tasks will get you across the basics of the typing module. 

But don't stop there. Use this repo to create new examples and challenges to deepen your understanding of PEP 0484.
   
## Make tasks

Run `make lint` to lint the code in this directory and `make type-check` to have mypy check your Python files.
    
## Resources you might need

### Multiple Python versions on OSX with Homebrew
If you're on OSX, use homebrew and want to install multiple Python 3 versions, check out https://bit.ly/brew-multi-python.

### Install mypy from source if using Python 3.5
The `requirements.txt` file installs mypy-lang from source so that it's compatible with Python 3.5.
 * See https://bit.ly/mypy-python35 for more information.
 
