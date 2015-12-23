# python-typing

Experimenting with defining and validating types in Python 3.5.

## Setup

Ensure you have Python 3.5 installed, then create a virtual environment targeting your installation of Python 3.5

    mkvirtualenv pytypes --python=/usr/local/bin/python3.5

Then install the required libraries (note that mypy-lang is installed from source so it is compatible with Python 3.5).

    `pip install -r requirements.txt'

Then you can test mypy is working by running `mypy main.py`.
    
## Resources you might need

### Multiple Python versions on OSX with Homebrew
If you're on OSX, use homebrew and want to install multiple Python 3 versions, check out https://bit.ly/brew-multi-python.

### Install mypy from source if using Python 3.5
 * See https://bit.ly/mypy-python35 for why
 * Add `git+git://github.com/JukkaL/mypy.git` to your requirements file.
