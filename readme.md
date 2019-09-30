# FakeTube 
## A simple Django/MongoDB system to solve the Deeper Systems test

### How to execute

Go to the folder via CMD and create a Virtual Enviroment



	python -m venv venv


Go to the ***venv/Scripts*** directory via CMD and execute the ***activate.bat***:


    C:\ ... >cd venv
    C:\ ... \venv > cd Scripts
    C:\ ... \venv\Scripts> activate.bat


You should see a **(venv)** before the directory address

	(venv) C:\ ... \venv\Scripts> 

Go back to your project main folder

	C:\ ... \venv\Scripts> cd ..
	C:\ ... \venv > cd ..
    C:\ ... >

Install the required modules

	pip install -r requirements.txt

Serve the project

	python manage.py runserver

Finally, in your browser access **localhost:8000** and test at will =)
