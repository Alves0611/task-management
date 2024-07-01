# Task Management API

## Overview

This project is a Task Management API built using Flask. The API allows users to create, read, update, and delete tasks. It also includes a comprehensive testing suite with `pytest` to ensure the reliability of the application.

![](/images/swagger.png)

## Features

- **Create Tasks**: Add new tasks with a title and description.
- **Retrieve Tasks**: Fetch all tasks or a specific task by ID.
- **Update Tasks**: Modify the details of an existing task.
- **Delete Tasks**: Remove tasks by ID.
- **Comprehensive Testing**: Ensure the reliability of the application with `pytest`.

## Requirements

- Python 3.8+
- Flask 2.3.0
- Werkzeug 2.3.0
- requests 2.31.0
- pytest 7.4.3
- bandit 1.7.5
- flake8 4.0.1

## Installation

1. **Clone the repository**:
```bash
  git clone https://github.com/Alves0611/task-management

  cd task-management
```

2. **Create a virtual environment and activate it**:

```bash
  python -m venv venv

  source venv/bin/activate
```

3. **Install the dependencies:**:

```bash
  pip install -r requirements.txt
```

## Running Tests
```bash
    make test
```


![](/images/pytest.png)
