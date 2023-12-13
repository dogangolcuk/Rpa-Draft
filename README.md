# QRPA Engine (Temporary Name)

## Overview

Introducing QRPA Engine, a sophisticated Python framework designed for automation purposes. This powerful engine aims to replicate human-like actions on a computer system while efficiently executing a wide range of tasks. Leveraging APIs whenever possible, QRPA Engine prioritizes seamless and discreet task execution.

## Detailed Description

Introducing QRPA Engine, a sophisticated Python framework designed for automation purposes. Its primary objective is to emulate human-like actions on a computer system while efficiently executing various tasks. Leveraging APIs whenever possible, QRPA Engine prioritizes seamless task execution in a silent manner.

This powerful framework orchestrates tasks in a sequential flow, facilitating the smooth transfer of data between these tasks. Each task incorporates data manipulation capabilities via externally injected plugins, ensuring enhanced flexibility and extensibility. The logging mechanism captures comprehensive step-by-step details, offering invaluable insights for debugging purposes.

For RPA developers seeking comprehensive oversight, QRPA Engine provides the option to record the screen during specific task executions, allowing for detailed monitoring from initiation to completion. The plugin system within QRPA Engine empowers users to load diverse plugins, further augmenting data manipulation capabilities and task flexibility.

Sending tasks to QRPA Engine is streamlined through the utilization of sendflow.py, enabling a seamless and efficient interaction with the framework. QRPA Engine stands as a comprehensive and adaptable solution for automating intricate tasks with precision and reliability.

## Features

- **Task Orchestration:** Seamlessly executes tasks in a sequential flow.
- **Data Transfer:** Facilitates smooth data transfer between tasks.
- **Plugin Integration:** Allows external plugins for data manipulation, enhancing flexibility.
- **Logging Mechanism:** Captures detailed step-by-step logs for debugging purposes.
- **Screen Recording:** Option to record screen during specific task executions for oversight.
- **Interaction:** Utilizes `sendflow.py` for efficient interaction with the framework.

## Setup Programming Environment 🚀

Follow these steps to set up the programming environment:

1. **Install Python 3.x**
2. **Virtual Environment Setup:**
    - Install `virtualenv` if not installed: `pip install virtualenv`
    - Create a virtual environment: `python3 -m venv rpaenv`
    - Activate the virtual environment:
      - On Windows: `rpaenv\Scripts\activate`
      - On Linux: `source rpaenv/bin/activate`
3. **Install Requirements:**
    - For Development: `pip install -r requirements.txt`
    - For Production: `pip freeze > requirements.txt`
4. **Package Management:**
    - List installed packages: `pip list`
    - Check for outdated packages: `pip list --outdated` or `pip-check`
    - Update packages: `pip install -U pip` and `pip install -U -r requirements.txt`
5. **Running the Script:**
    - Start the engine: `python3 QRPAEngine.py`
    - Send tasks using `sendflow.py`: `python3 sendflow.py tasks/task.json`

## Roadmap & History ⏲️

### Implemented Features

- **06.12.2023:** Initial version
- **07.12.2023:** Added logging mechanism, separated main to libs, and image search functionality.
- **08.12.2023:** Introduced workflow mechanism, tasks, snaps folders, and screen recording feature.
- **09.12.2023:** Integrated plugin system, JSON-based flows, and `sendflow.py` for task submission.
- **10.12.2023:** Added system tray functionality for starting and stopping the server, addressed plugin load and sys.exit issues.

### To Be Implemented

- **Plugin Expansion:** Enhance plugin system for additional functionalities.
- **Enhanced GUI:** Develop an intuitive user interface for improved interaction.
- **Advanced Logging:** Incorporate advanced logging features for comprehensive debugging.
- **Task Scheduler:** Introduce a scheduler for task automation at specific intervals.
- **Error Handling:** Implement robust error handling mechanisms for improved stability.

## Contributing

Your contributions are welcome! Please follow the contribution guidelines outlined in CONTRIBUTING.md to contribute to this project.

- Create SSH key for GitHub
    > ssh-keygen

- Copy the public key to GitHub account
  > cat .\.ssh\id_rsa.pub

- Set remote GitHub URL
    > git remote set-url origin <git@github.com>:qsoft-git/zozi-automate-agent-arge.git
    > git remote add personal <git@github.com>:dogangolcuk/testRPA_1.git

- Push to Remote
    > git push personal master
    > git push origin master

- Now you can push your changes to GitHub
  > git add .
  > git commit -m "Initial commit"
  > git push origin master
  > git push personal master

## License

This project is licensed under the [LICENSE NAME] - see the [LICENSE.md](LICENSE.md) file for details.

## QSOFT

This project is maintained by QSOFT Team, a software development company specializing in innovative automation solutions. For inquiries or collaborations, please contact us at [contact@qsoft.com.tr](mailto:contact@qsoft.com).
