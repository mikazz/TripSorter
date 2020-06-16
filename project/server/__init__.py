# project/server/__init__.py


import os
from flask import Flask
from flask_bootstrap import Bootstrap

from flask_mongoengine import MongoEngine
# from flask_sqlalchemy import SQLAlchemy

# instantiate the extensions
bootstrap = Bootstrap()
db = MongoEngine()  # SQLAlchemy()

CONFIG = "LOCAL"
# CONFIG=prod; python run.py


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__,
        template_folder="../client/templates",
        static_folder="../client/static",
    )
    
    #import os
    #if os.environ['CONFIG'] == 'prod':
    #    config = ProductionConfig()
    #else:
    #    config = DevelopmentConfig()

    if CONFIG == "DOCKER":
        # Set docker configuration (from environmental variables like casted by docker-compose.yml)
        app_settings = os.getenv("APP_SETTINGS")
        app.config.from_object(app_settings)

    elif CONFIG == "LOCAL":
        import rq_dashboard
        # Set local configuration (from inside app config.py)
        app.config.from_object('project.server.config.LocalConfig')
        # RQ Dashboard configuration
        #app_settings = os.getenv("APP_SETTINGS")
        #app.config.from_object(app_settings)
        app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

    # set up extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # register blueprints
    from project.server.main.views import main_blueprint

    app.register_blueprint(main_blueprint)

    # shell context for flask cli
    app.shell_context_processor({"app": app, 'db': db})

    return app
