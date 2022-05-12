# Python Exercise

## General Instructions

For this exercise, you are provided a starting code with empty function declarations for each of the questions in your ticket. These functions are located in the [generate_schedule_c/schedule.py](generate_schedule_c/schedule.py) file.
We've also provided [a small application server](app.py) that we can use to test your code. Please do not modify this file.

## System Requirements

The current recommended [Python](https://www.python.org/downloads) is **3.9.12** or higher.

## Development

### Development Environment Setup

#### Prerequisites

- Install [Python](https://www.python.org/downloads)
- In the command line, navigate to the `server` directory of the project. Then follow these steps:

#### 1. Create a virtual environment for your project:

Linux/MacOS
```
python3 -m venv venv
```

Windows
```
python -m venv venv
```

#### 2. Activate your virtual environment:

Linux/MacOS
```
source venv/bin/activate
```

Windows
```
venv\Scripts\activate.bat
```

#### 3. Install the dependencies:

Linux/MacOS/Windows
```
python -m ensurepip --upgrade
python -m pip install -r requirements.txt
```

### Running the application

Three commands have been provided for you to test your function implementations with the hardcoded data. These commands will log out the return value of your functions.

First change your directory to `generate_schedule_c`:

```
cd generate_schedule_c
```

To run `generate_schedule_c1` for question 1:

```
python generate_schedule_c1.py
```

To run `generate_schedule_c2` for question 2:

```
python generate_schedule_c2.py
```

### Format code

Please format your code before making a pull request to make it easier for us to review the code.
Change your directory to `generate_schedule_c` and run:

```
python -m black .
```

### Running tests

There are some basic test cases to check
that you understand the ticket instructions.
You can run the test code with this command:

```
pytest tests/
```

