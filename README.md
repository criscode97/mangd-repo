# mangd
A server-side CRUD built with Python and Flask.

## Live Demo
Upcoming. Having issues with deployment at the momment


## Technologies
- Python: v3.10.1
- Flask: v2.0.2
- Authlib: v0.15.5
- Bootstrap: v5.0
- HTML5
- CSS: V2.1
- Javascript: ECMAScript 2021
- Moment.js: v2.29.1
- Flask-Mail: v0.9.1
- Flask-SQLAlchemy: v2.5.1
- google-api-python-client: v2.33.0
- google-auth-oauthlibv: v0.4.6
- itsdangerous: v2.0.1
- protobuf: v3.19.1
- Werkzeug: v2.0.2
- Flask-Session: v0.4.0
- 

## Features
This Server-side application allows user to register by creating a username and password and providing an email.
The user can also login using the google login option.
The user can create a todo item and add a deadline if they wish
Everytime the user provides a deadline, the app automatically syncs it to their calendar and saves the id of the item so it can be deleted by the user later on.
The user can filter the list of todos using the filter by option


## App structure

mangd-repo  
│   .gitignore  
│   Procfile  
│   README.md  
│   requirements.txt  
│   run.py  
│  
└───mangd  
    │   client_secret.json  
    │   config.py  
    │   database.py  
    │   extras.py  
    │   googlecalendar.py  
    │   user.sqlite3  
    │   __init__.py  
    │  
    ├───static  
    │       style.css  
    │  
    ├───templates  
    │       api.html  
    │       forgotpassword.html  
    │       layout.html  
    │       login.html  
    │       register.html  
    │       resetpassword.html  
    │       todos.html  
    │  
    ├───todos  
    │       routes.py  
    │       __init__.py  
    │  
    └───users  
            routes.py  
            __init__.py  
          
## UML
<img width="816" alt="2021-11-02 (11)" src="https://user-images.githubusercontent.com/92554847/146624827-f699f878-0504-41dc-bcc2-108d5e1559ee.png">


## screenshots


![Screenshot (12)](https://user-images.githubusercontent.com/92554847/146624834-5a89fba9-be6f-4f2b-a27b-c62fbed96b8d.png)
![Screenshot (13)](https://user-images.githubusercontent.com/92554847/146624835-a19fa52f-66b8-45f3-9d36-0ee4d09f2974.png)
![Screenshot (14)](https://user-images.githubusercontent.com/92554847/146624843-84ccca8d-317c-46e7-8a33-0147b29c41bc.png)
![Screenshot (15)](https://user-images.githubusercontent.com/92554847/146624844-58b455e3-6a52-469e-ba08-86cacfec0749.png)
![Screenshot (16)](https://user-images.githubusercontent.com/92554847/146624846-69a58210-106e-4b43-90de-438e403056ab.png)
![Screenshot (17)](https://user-images.githubusercontent.com/92554847/146624849-a05e160c-f48a-4a21-a255-022568fd1fb8.png)
![Screenshot (18)](https://user-images.githubusercontent.com/92554847/146624851-ce9ab88e-0b8e-4c1d-a18d-80b96d57fd8b.png)
![Screenshot (19)](https://user-images.githubusercontent.com/92554847/146624852-d4df5a08-40ed-46fb-bd5a-471bd74bb2a9.png)
