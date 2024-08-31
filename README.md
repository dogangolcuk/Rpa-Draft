# RPA Engine (Temporary Name)

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
    - Start the engine: `python3 RPAEngine.py`
    - Send tasks using `sendflow.py`: `python3 sendflow.py tasks/task.json`
