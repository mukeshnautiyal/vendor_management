# vendor_management
python version-3.8.7
Django version - 4.2.8
djangorestframework version 3.14.0

Setup application
- Install specified python version on local machine

- Create python virtual environment using below command

    virtualenv your_env_name(install virtual env dependency if it's not installed)

- Activate the above created env using below command inside the env

    window - \.scripts\activate

    ubuntu - source env_name/bin/activate(outside the env folder)

    anaconda- conda activate env_name (outside the env folder)

- Run the below command to install project requirements

    pip install -r requirements.txt

- Create new database in the mysql DB(as i'm using mysql database) 

- create .env file inside the project directory and keep the all Database related key value inside the env file as given in the sampleenv file

- Rename the file name settings1.py to settings.py and add the database related information in the .env file

- Create new migration if not exist in the project directory

    Python manage.py makemigrations

- To migrate the above created migration use below command

    Python manage.py 
    
- Create super user for the admin access and API's permissions

    python manage.py createsuperuser

- If every thing is working fine then run the below command to start application on local

    python manage.py runserver

- Vendor Management.postman_collection.json is added in the project directory import in the postman and test the all API's end point.

- run the test cases using below command

    python manage.py test vendor