from pages.login_page import LoginPage

from utils.config_reader import ConfigReader


def test_valid_login(page):

    config = ConfigReader.read()

    page.goto(config["url"])

    login = LoginPage(page)

    login.login(
        config["username"],
        config["password"]
    )
    print("URL:", page.url)
    print("Title:", page.title())

    assert login.dashboard_loaded()
