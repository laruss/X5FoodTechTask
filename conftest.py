import pytest
from mocks.api import create_app


@pytest.fixture
def app():
    """ fixture to start a mock """
    app = create_app()
    return app
