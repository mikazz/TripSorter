# project/server/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# # JSON-based secrets module. Remember to Add the secrets file name to the .gitignore or .hgignore
# with open("secrets.json") as f:
#     secrets = json.loads(f.read())
#
#
# class ImproperlyConfigured(Exception):
#     pass
#
#
# def get_secret(setting, secrets=secrets):
#     """
#         Get the secret variable or return explicit exception.
#     """
#     try:
#         return secrets[setting]
#     except KeyError:
#         error_msg = "Set the {0} environment variable".format(setting)
#         raise ImproperlyConfigured(error_msg)


class LocalConfig:
    """Local configuration."""
    REDIS_URL = "redis://127.0.0.1:6379/0"
    MONGODB_HOST = "mongodb://localhost:27017"

    QUEUES = ["default"]
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    #RQ_DASBOARD_URL = "127.0.0.1:9181"
    SECRET_KEY = "SECRET"  # get_secret("SECRET_KEY")
    FLASK_SECRET = SECRET_KEY


class BaseConfig:
    """Base configuration."""
    TESTING = False
    DEBUG = False
    WTF_CSRF_ENABLED = True
    REDIS_URL = "redis://redis:6379/0"
    MONGODB_HOST = "mongodb://mongodb:27017"
    QUEUES = ["default"]
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    # THIS APP IS IN DEBUG MODE. NOT FOR PRODUCTION
    WTF_CSRF_ENABLED = False
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configurations"""
    DEBUG = False


class TestingConfig(BaseConfig):
    """Testing configuration."""
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
