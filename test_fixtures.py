import pytest



@pytest.fixture
def browser():
    print ("Браузер!")

    yield

    print ("закрываем браузер!")
@pytest.fixture
def login_page (browser):
    print("Лоогин пейдд!")
    pass

@pytest.fixture
def user():
    print("Юзер!")
    return "username", "password"

def test_login(login_page, user):
    username, password = user
    assert username == "username"
    assert password == "password"

