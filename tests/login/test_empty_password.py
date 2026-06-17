from pages.login_page import LoginPage

from utils.config_reader import ConfigReader


def test_empty_password(page):

    config = ConfigReader.read()

    page.goto(config["url"])

    login = LoginPage(page)

    login.login(
        config["username"],
        ""
    )

    assert login.password_validation_visible()