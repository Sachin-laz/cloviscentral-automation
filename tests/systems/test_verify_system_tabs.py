from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from pages.systems_page import SystemsPage


def test_verify_system_tabs(page):

    config = ConfigReader.read()

    page.goto(config["url"])

    login = LoginPage(page)

    login.login(
        config["username"],
        config["password"]
    )
    print("URL:", page.url)
    print("Title:", page.title())

    systems = SystemsPage(page)

    assert systems.open_systems()

    assert systems.verify_system_tabs(), \
        "Pending, Active and Inactive tabs are not displayed."