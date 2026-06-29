from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from pages.dashboard_page import DashBoardpage
from pages.clients_page import ClientsPage

def test_dashboard_customer_count(page):

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

    actual_count = clients.get_client_count()

    dashboard = DashBoardpage(page)

    dashboard.open()

    dashboard_count = dashboard.get_dashboard_client_count()

    assert actual_count == dashboard_count