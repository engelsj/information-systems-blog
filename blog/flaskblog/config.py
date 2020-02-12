import os


class Config:
    SECRET_KEY = os.environ.get('KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('PASSWORD_USER')