from pages.login_page import LoginPage
from pages.systems_page import SystemsPage
from utils.config_reader import ConfigReader


def test_verify_invalid_system_search(page):

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

    assert systems.search_system("Invalid123"), \
        "Failed to perform search."

    assert systems.verify_no_data_found(), \
        "No Data Found message is not displayed."

    assert systems.clear_search(), \
        "Failed to clear the search."