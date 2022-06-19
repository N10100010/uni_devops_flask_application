import pytest

from uni_devops_showcase.uni_devops_flask_application.src.server import app


@pytest.fixture
def test_client():
    app.testing = True
    return app.test_client()
