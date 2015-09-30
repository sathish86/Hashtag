Technologies used:
==================

1. Python
2. Django and tastypie for API.
3. AngularJS

Development environment:
========================

Linux system

Steps to run the project:
=========================

Step 1. Unzip the project "note_hashtag.zip".

Step 2: Install virtual environment using the below command.

"pip install virtualenv"

Refer the below link to know more about virtual environment.

http://docs.python-guide.org/en/latest/dev/virtualenvs/


Step 3:

Get into the project folder "note_hashtag" and create virtual environment using 
"virtualenv venv"

Activate the virtual environment with the below command.
"source venv/bin/activate"


Step 4:

Install required libraries in virtual environment using the below command.

"pip install -r requirements.txt"


Step 5:

Create database and relevant tables using

"python manage.py migrate"


Step 6:

Run the project using

"python manage.py runserver"



Step 7:

Open below URL in the browser.

"http://localhost:8000/notes/"




