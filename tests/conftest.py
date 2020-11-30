import os
import pytest
import tempfile
from app import create_app
from tests.functionsforPytest import path
from config import Config

path = path()

@pytest.fixture
def TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/finance.db'.format(path)


@pytest.fixture
def app():
    #""Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app(Config)
    yield app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()