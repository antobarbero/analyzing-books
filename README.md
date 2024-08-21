# Analyzing books

## Overview

Analyzing and visualizing different aspects of books from the "goodbooks" dataset using PySpark.

- How book popularity changes over time and identifying trends in reading preferences.
- Exploring common words and phrases used in book titles and descriptions.

Dataset available here: https://github.com/zygmuntz/goodbooks-10k

The implementation follows the Modular Pipeline Pattern, and the flow is more or less:
Data Ingestion → Data Cleaning → Data Transformation → Reporting/Visualization

The module `run_pipeline.py` orchestrates the entire pipeline, connecting all layers.


## Installation for developers

### Prerequisites

1 - Install Python 3.11+ (https://www.python.org/downloads/)

2 - Install pipx (https://pipx.pypa.io/stable/installation/)

*Linux:*  
`python3 -m pip install --user pipx`

*Windows:*
`py -m pip install --user pipx`

It is possible the above finishes with a WARNING looking similar to this:
WARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH

If so, go to the mentioned folder, allowing you to run the pipx executable directly. Enter the following line 
(even if you did not get the warning):
.\pipx.exe ensurepath
This will add both the mentioned above path and the %USERPROFILE%\.local\bin folder to your search path. 
Restart your terminal session and verify pipx does run.


**For other installation options check the link above.**


3 - Install Poetry for dependency management (https://python-poetry.org/docs/#installation):
`pipx install poetry`

4 - Install Git Large File Storage, for storing the datasets in a more efficient way (https://git-lfs.com/)

### Setup

1 - Clone the repository

2 - Create a virtualenvironment and install dependencies with poetry by running this command:

`poetry install`

3 - Activate the created virtual environment (.venv) 

Windows: `.venv\Scripts\activate`

Or set the created virtual environment as your project interpreter and open a new terminal to have it activated.

(in pycharm: Settings -> Python Interpreter -> add local 
  -> Select 'Existing'-> Select "analyzing_books\.venv\Scripts\python.exe)

4 - Run `git lfs install`

For tracking additional files use `git lfs track *.csv`

5 - Before contributing, install the pre-commit hooks by running the following command:

`pre-commit install`

This will automatically execute some hooks when you commit your changes
to format the code, checking complexity, typehints, etc.
You can see all the activated hooks in the `.pre-commit-config.yaml` file.

### Run tests

#### With pytest

Execute this command in your terminal with the poetry virtual environment activated:

`pytest tests`
