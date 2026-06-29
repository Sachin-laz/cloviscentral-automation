from pages.login_page import LoginPage
from pages.systems_page import SystemsPage
from utils.config_reader import ConfigReader


def test_verify_valid_system_search(page):

    config = ConfigReader.read()

    page.goto(config["url"])

    login = LoginPage(page)

    login.login(
        config["username"],
        config["password"]
    )

    systems = SystemsPage(page)

    assert systems.open_systems(), \
        "Failed to open Systems page."

    assert systems.search_system("Akash Board"), \
        "Failed to search the system."

    assert systems.verify_search_result("Akash Board"), \
        "Search result does not match the expected system."

    assert systems.clear_search(), \
        "Failed to clear the search."