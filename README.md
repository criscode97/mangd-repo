# mangd
A server-side CRUD built with Python and Flask.

## Live Demo
Linode cloud deployment using gunicorn, nginx, and supervisor: http://www.mangdtodos.com/


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
The user can create a todo item and add a deadline if they wish
Everytime the user provides a deadline, the app automatically syncs it to their google calendar and saves the id of the item so it can be deleted by the user later on.
The user can filter the list of todos using the filter by option.


## App structure
```bash
mangd-repo  
│   .gitignore  
│   Procfile  
│   README.md  
│   requirements.txt  
│   run.py  
│  
└───mangd  
    │   config.py  
    │   database.py  
    │   extras.py    
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
    ├───users  
    |        routes.py  
    |        __init__.py 
    └───googleapi
            routes.py
            client_secret.json
            __init__.py
    
```        
## UML
<img width="816" alt="2021-11-02 (11)" src="https://user-images.githubusercontent.com/92554847/146624827-f699f878-0504-41dc-bcc2-108d5e1559ee.png">

