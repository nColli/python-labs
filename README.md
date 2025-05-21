# python-labs

## Virtual enevironment

Create a new virtual environment (inside the directory)
    `python3 -m venv env`

Activate env
    `source env/bin/activate`

Deactivate env
    `deactivate`

View packages in the current env
    `pip list`

Installing packages
    `pip install requests`

Saving dependencies
    `pip freeze > requirements.txt`

Example Work Flow (env is usually added to .gitignore)
    `pip install -r requirements.txt`
