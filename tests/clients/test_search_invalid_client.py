from pages.login_page import LoginPage
from pages.clients_page import ClientsPage
from utils.config_reader import ConfigReader


def test_invalid_search_client(page):

    config = ConfigReader.read()

    page.goto(
        config["url"],
        wait_until="domcontentloaded",
        timeout=60000
    )

    login = LoginPage(page)

    login.login(
        config["username"],
        config["password"]
    )

    clients = ClientsPage(page)

    clients.open()

    clients.search_client(
        "INVALID_TEST_123456789"
    )

    assert clients.is_no_data_found_displayed()