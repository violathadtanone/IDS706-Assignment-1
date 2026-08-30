# IDS 706: Python Template 27 Aug 2026

## Project Description
This is the first assignment for IDS 706. This python template will be the baseline for future projects.

## Project Structure 
```bash
IDS706-Assignment-1/
├── requirements.txt         # List of packages required for installation
├── src/                     
│   ├── main.py              # Start/Run of the overall application
├── tests/                   
│   ├── test_main.py         # Project main test file
├── Makefile                 # Create shortcut to all common command for the development
├── Dockerfile               # Docker container to package everything we built
├── .dockerignore            # Indicate files that should be ignored by Docker
├── .github/                   
│   ├── workflows        
│       ├── test.yml         # GitHub Actions workflow



└── README.md                # Project documentation







├── .github/workflows/       # CI/CD configuration
├── .devcontainer/           # Development environment setup
```

## Setup Instructions 
### 1. Creat GitHub repository
General:
- Name the repository with IDS706-Assignment-1

Configuration:
- Add README - Toggle On
- Add .gitignore - Select Python
- Proceed to create repository
<br><br>

### 2. Clone repository in VS Code
- Open Command Palette and select Git: Clone
- Paste GitHub repository URL (e.g. https://github.com/violathadtanone/IDS706-Assignment-1)
- Select the local folder to continue the development
<br><br>

### 3. Set up a Python virtual environment
This step will create a separate virtual environment, where all the packages installations for the project will be in this environment to avoid conflict with other projects.
- Create and activate the virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Upgrade pip
pip is Python package manager. Upgrading pip will ensure that it is compatible with the current Python version before installing other packages
```bash
python -m pip install --upgrade pip
```
<br><br>

### 4. Create requirement file for pytest
- Create a new file called `requirements.text` and add packages below in the file
```
pytest
black
ruff
```

- Install the requirements
```bash
python -m pip install -r requirements.txt
```

- Verify that `pytest` is installed. This should return with pytest version number on Terminal
```bash
pytest --version
```
<br><br>

### 5. Run the welcome message example
Creat source file:
- Create the folder name `src` in the project root. This is the folder to store all the source codes.
- Create a new file called `main.py` under this folder and include the code below. This is the main part of the application.
```
def welcome_message(name):
    return f"{name}, welcome to the Data Engineering course."

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(welcome_message(name))

def setting_goals(point):
    return f"Let's try together to earn {point} points!"

if __name__ == "__main__":
    point = input("How many points you are aiming for this assignment?: ")
    print(setting_goals(point))
```

Creat test file:
- Create the folder name `tests` in the project root. This is the folder to store all the test files.
- Create a new file called `test_main.py` under this folder and include the code below. This is the main file to be used for testing
```
from src.main import welcome_message, setting_goals

def test_welcome_message():
    assert welcome_message("Ammy") == "Ammy, welcome to the Data Engineering course."
    
def test_setting_goals():
    assert setting_goals("200") == "Let's try together to earn 200 points!"
```

- Run the code below to check whether the source file and test file are working properly
```bash
python -m pytest -vv
```

- We can also add `-vv`, if we want to see further testing details
```bash
python -m pytest -vv
```
<br><br>

### 6. Create a Makefile
In a GitHub repository, a Makefile is used to automate repetitive development (e.g. install, test or run). The complex command will now by grouped into short, reusable shortcuts. 
- Create a new file called `Makefile` in the project root with the code below. The file should have Orange icon.
```
.PHONY: install test run docker-build docker-run docker-test clean

IMAGE_NAME := data-engineering-demo

# Install dependencies
install:
	python -m pip install -r requirements.txt

# Run tests
test:
	python -m pytest -q

# Run the application
run:
	python src/main.py

# Build the Docker image
docker-build:
	docker build -t $(IMAGE_NAME) .

# Run the application inside Docker
docker-run:
	docker run -it --rm $(IMAGE_NAME)

# Run the test suite inside Docker
docker-test:
	docker run --rm $(IMAGE_NAME) python -m pytest -q

# Clean generated files
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache

# Format Python code to help with code structure
format:
	python -m black src tests

# Lint Python code for identifying code problems (e.g. unused packages or variables)
lint:
	python -m ruff check src tests    
```

- Verify that `make` is installed. This should return with GNU Make version number on Terminal
```bash
make --version
```

- Try the short cut that we built
Now instead of writing the full bash code such as `python -m pip install -r requirements.txt`, we can just write `make install`.
```bash
make install
make test
make run
make clean
make format
make lint
```
<br><br>

### 7. Run the project with Docker
Docker creates a container and packages everything we built together including python code, packages required and configuration.
This will allow others that may not have python to also run our application consistently.

- Install and open Docker Destop.
- Verify that Docker is installed. This should return with Docker version number on Terminal
```bash
docker --version
```
- Create a new file called `Dockerfile` in the project root and include the code below. The file should have Docker icon.
```
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY tests ./tests

CMD ["python", "src/main.py"]
```

- Create a another file called `.dockerignore` in the project root and include the code below. This summarises all the files to be ignored by Docker.
```
.venv
__pycache__
.pytest_cache
.git
.github
```

- Build the image using Docker related shortcut from `Makefile`
```bash
make docker-build
```

- Now we can run and test the application inside the container
```bash
make docker-test
make docker-run
```
<br><br>

### 7. Add GitHub Actions
We will create GitHub Actions workflow. Here, we are telling GitHub what to do once we push the code. The general idea here is:
→ GitHub starts workflow
→ Create Ubuntu machine
→ Download repository
→ Install python and its dependency
→ Run test from `Makefile`
→ Create Docker image and run the test again in the container


- Create the folder called `.github` in the project root and create another subfolder called `workflows`
- Create the file called `test.yml` within `workflows` and include the code below
```
name: Python tests

on:
    push:
    pull_request:
    workflow_dispatch:

jobs:
    test:
        runs-on: ubuntu-latest

        steps:
            - name: Check out repository
                uses: actions/checkout@v4

            - name: Set up Python
                uses: actions/setup-python@v5
                with:
                    python-version: "3.12"

            - name: Install dependencies
                run: make install

            - name: Run tests
                run: make test

            - name: Build Docker image
                run: make docker-build

            - name: Run tests in Docker
                run: make docker-test
```
<br><br>

### 8. Push and test GitHub Actions
This is a common command, when we are collaborating on codes on GitHub repository.

- Normally, when we are working with other people. We will pull the current repository first since there may be changes from our previous pull.
If there is no change, the output will mention `Already up to date.`
```bash
git pull
```

- We can also check the status of current reposiory using the code below.
```bash
git status
```

- Staging: Before pushing, we need to take all changes in the current folder and put them into the Git staging area.
```bash
git add .
```

- Commit: This will say all staged changes as a local commit
```bash
git commit -m "Add project files"
```

- Push: This will upload all commits to the reposity on GitHub.
```bash
git push
```
