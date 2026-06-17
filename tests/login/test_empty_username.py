from pages.login_page import LoginPage

from utils.config_reader import ConfigReader

def test_empty_username(page):

    config = ConfigReader.read()

    page.goto(config["url"])

    login = LoginPage(page)

    login.login(
        "",
        config["password"]
    )

    assert login.username_validation_visible()