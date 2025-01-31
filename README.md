# Django Forms Application

## Project Overview
This is a Django application for creating, updating, and deleting forms, with data displayed from an SQLite database. The application allows users to manage form submissions easily and view the data in a user-friendly interface.

## Prerequisites
Before running the project, ensure you have the following installed:

- **Python**: Version 3.x (You can download it from [python.org](https://www.python.org/downloads/))
- **Django**: Version 3.x or higher (This will be included in the `requirements.txt` file)

## Running the Project on Ubuntu
1. Install Python and pip:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2. Navigate to the project directory:
    ```bash
    cd django-forms-app
    ```

3. Install the required packages:
    ```bash
    pip3 install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python3 manage.py migrate
    ```

5. Collect static files:
    ```bash
    python3 manage.py collectstatic
    ```

6. Run the development server:
    ```bash
    python3 manage.py runserver 0.0.0.0:8000
    ```

7. Access the application in your browser at `http://<your-ubuntu-ip>:8000`
