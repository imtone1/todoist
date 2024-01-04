import pytest
from unittest.mock import Mock
from todoist_api_python.api import TodoistAPI
from todoist_api_app.todoist import get_one_project

from muuttujat import *

VALID_PROJECT_ID = "1534016463"

@pytest.fixture
def api():
    return TodoistAPI(TODOIST_API_KEY)

def test_get_one_project(api):
    api.get_one_project = Mock(return_value=VALID_PROJECT_ID)
    assert get_one_project(api, VALID_PROJECT_ID) == VALID_PROJECT_ID