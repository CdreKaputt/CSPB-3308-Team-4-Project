class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEV_DATABASE_URL")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
