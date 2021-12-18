from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from authlib.integrations.flask_client import OAuth
from mangd.config import config_app

application = config_app()
mail = Mail(application)
oauth = OAuth(application)
db = SQLAlchemy(application)



from mangd.users.routes import users
from mangd.todos.routes import todos_app

application.register_blueprint(users)
application.register_blueprint(todos_app)
# with application.application_context():
#     db.create_all()

    


