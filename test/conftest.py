import pytest

from test import EmployeeFactory


@pytest.fixture
def base_url():
    return 'http://128.199.158.232:8002'


@pytest.fixture
def list_create_url(base_url):
    return base_url+'/employees'


@pytest.fixture
def employee_dict():
    return EmployeeFactory().__dict__
