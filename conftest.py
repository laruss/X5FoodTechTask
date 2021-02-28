import pytest
from mocks.api import create_app


@pytest.fixture
def app():
    app = create_app()
    return app
