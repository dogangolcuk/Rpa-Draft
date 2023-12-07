# Setup Programming Environment 🚀

- Install Python 3.x
- Make a virtual environment for development
  - > pip install virtualenv
  - > python3 -m venv rpaenv
    - on Windows
        > rpaenv\Scripts\activate
      - if not activated on windows because of permission issue open as admin command prompt run code
           > Set-ExecutionPolicy RemoteSigned
    - on Linux
        > source rpaenv/bin/activate
- Install requirements for development
    > pip install -r requirements.txt
- Make requirements for production
    > pip freeze > requirements.txt
- List packages
    > pip list
- Check outdated packages
  - > pip list --outdated
  - > pip-check
- Update packages
  - > pip install -U pip
  - > pip install -U -r requirements.txt
- Run script
  - > python3 main.py