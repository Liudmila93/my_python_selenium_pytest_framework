# my_python_selenium_pytest_framework
This framework contains test scripts written in Python.
Used Selenium and PyTest.
For report generation used Allure

# Installation
pip install -r requirements.txt

# How to run tests
pytest -v -s --browser "chrome" tests/test_login.py

# How to get allure reports:
1. run in terminal: pytest --alluredir=allure_reports tests/test_login.py
2. receive results: allure serve allure_reports

# Username and password
To make username and password secured it is located in .env file.
.env file is in gitignore.
So when you clone the repository - create .env file in the root directory with
LOGIN=login
PASSWORD=password


