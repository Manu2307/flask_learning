import pytest
from tut1.sample import Student, Engineer
from datetime import datetime


@pytest.fixture
def dummy_student(request):
    return Student("Manoj", datetime(2000, 9, 26), "Software Engineer", request.param)


@pytest.fixture
def make_dummy_engineer():
    def _make_dummy_engineer(name, experience):
        return Engineer(name, datetime(2000, 9, 26), "software engineer", experience)
    return _make_dummy_engineer
