from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')


class DeveleopmentConfig(Config):
    DEBUG = True


config = {
    'development': DeveleopmentConfig
}
