import os


class Config:
    SECRET_KEY = '3a3b38746b050db4ff2766ce44791cf8'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1997@db:5432/flaskblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')