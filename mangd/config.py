# user related imports
import os

from flask import Flask
from flask_session import Session


#app configuration
def config_app(test_config=None):
    app = Flask(__name__, static_folder="/static")
    app.config.from_mapping(
        # app configuration
        SECRET_KEY=os.urandom(12),
        SECURITY_PASSWORD_SALT=os.urandom(20),
        SESSION_TYPE="filesystem",
        DEBUG=True,
        SESSION_PERMANENT=False,
        OAUTHLIB_INSECURE_TRANSPORT="1",
        # SQLAlchemy configuration
        SQLALCHEMY_DATABASE_URI="sqlite:///user.sqlite3",
        SQLACLCHEMY_TRACK_MODIFICATIONS=False,
        # Flask-Mail configuration,
        MAIL_PORT=25,
        MAIL_SERVER="smtp.gmail.com",
        MAIL_USE_TLS=True,
        MAIL_USERNAME=os.environ['MAIL_USERNAME'],
        MAIL_PASSWORD=os.environ['MAIL_PASSWORD'],
    )
    sess = Session(app)
    sess.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app
