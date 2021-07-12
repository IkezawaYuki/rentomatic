import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """base configuration"""


class ProductionConfig(Config):
    """Production configuration"""


class DevelopmentConfig(Config):
    """Development configuration"""


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True


