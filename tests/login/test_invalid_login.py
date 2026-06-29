from pages.login_page import LoginPage

from utils.config_reader import ConfigReader

def test_invalid_password(page):

    config = ConfigReader.read()

    page.goto(config["url"])

    login = LoginPage(page)

    login.login(
        config["username"],
        "WrongPassword123"
    )

    assert login.invalid_login_message_visible()