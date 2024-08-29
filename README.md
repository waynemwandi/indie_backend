# INDIE Daraja Integration

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

This is an implementation of the Safaricom Daraja C2B and STK integration with Django python.

## Features

- Daraja C2B
- Daraja STK

## Installation

### Prerequisites

- Set up virtual environment

```bash
python -m venv venv
```

- Set up MySQL database:
  Download and Configure [MySQL and MySQL Workbench](https://dev.mysql.com/downloads/file/?id=526408)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/waynemwandi/indie_backend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd indie_backend
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python manage.py runserver
   ```

## Usage

Provide examples of how to use your project, including code snippets, screenshots, or instructions.

```bash
# Run Migrations
python manage.py makemigrations
python manage.py migrate
```

Database Configurations in settings.py as;

```python
DATABASES = {
   'default': {
      'ENGINE': os.getenv('DATABASE_ENGINE', 'django.db.backends.mysql'),
      'NAME': os.getenv('DATABASE_NAME'),
      'USER': os.getenv('DATABASE_USER'),
      'PASSWORD': os.getenv('DATABASE_PASSWORD'),
      'HOST': os.getenv('DATABASE_HOST'),
      'PORT': os.getenv('DATABASE_PORT'),
   }
}
```

## Contributing

## License

## Contact
