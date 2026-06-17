from pages.login_page import LoginPage

from utils.config_reader import ConfigReader



def test_empty_credentials(page):

    config = ConfigReader.read()

    page.goto(config["url"])

    login = LoginPage(page)

    login.login("", "")

    assert login.username_validation_visible()

    assert login.password_validation_visible()