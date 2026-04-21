import pytest
from src.util.dao import DAO

@pytest.fixture
def dao():
    dao = DAO("user")
    dao.drop()
    yield dao
    dao.drop()

@pytest.mark.integration
def test_create_valid_user(dao):
    data = {
        "firstName": "name",
        "lastName": "Test",
        "email": "name@test.com"
    }

    result = dao.create(data)

    assert result is not None
    assert result["firstName"] == "name"
    assert result["lastName"] == "Test"
    assert result["email"] == "name@test.com"
    assert "_id" in result

@pytest.mark.integration
def test_create_missing_field(dao):
    data = {
        "firstName": "name",
        "email": "name@test.com"
    }

    with pytest.raises(Exception):
        dao.create(data)

@pytest.mark.integration
def test_create_wrong_type(dao):
    data = {
        "firstName": "name",
        "lastName": "Test",
        "email": 12345 
    }

    with pytest.raises(Exception):
        dao.create(data)

@pytest.mark.integration
def test_create_duplicate_email(dao):
    data = {
        "firstName": "name",
        "lastName": "Test",
        "email": "name@test.com"
    }

    dao.create(data)

    with pytest.raises(Exception):
        dao.create(data)
