from pages.clients_page import ClientsPage
from testdata.client_data import ClientData
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader


def test_edit_customer(page):

    config = ConfigReader.read()

    customer = ClientData.valid_customer()

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

    customer = ClientData.valid_customer()

    while clients.verify_client_exists(customer["client_code"]):
        customer = ClientData.valid_customer()

    clients.add_customer(customer)

    assert clients.is_customer_saved_successfully()

    clients.search_client(customer["client_code"])

    clients.click_more_actions()

    clients.click_delete()

    assert clients.is_delete_dialog_visible()

    clients.confirm_delete()

    assert clients.is_customer_deleted_successfully()

    assert not clients.verify_client_exists(
        customer["client_code"]
    )