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
  - > python3 QRPAEngine.py
- Send tasks with sendflow.py
  - > python3 sendflow.py tasks/task.json

# History ⏲️

- 06.12.2023: Initial version
- 07.12.2023: Log mechanism, seperate main to libs , find image in image
- 08.12.2023: Workflow mechanism , tasks and snaps folders added, record screen flow added.
- 09.12.2023: Plugin system added. Flows send in Json format. sendflow.py added to send tasks to server.
- 10.12.2023: Systemtray added to start ,stop server.
