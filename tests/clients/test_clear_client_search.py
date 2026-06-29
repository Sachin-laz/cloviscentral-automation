from pages.login_page import LoginPage
from pages.clients_page import ClientsPage
from utils.config_reader import ConfigReader
from testdata.client_data import ClientData


def test_clear_search(page):

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

    customer = ClientData.valid_customer()

    clients.open()

    page.wait_for_timeout(1000)

    initial_count = clients.get_total_customer_count()

    print(f"{initial_count}")

    customer = ClientData.valid_customer()

    while clients.verify_client_exists(customer["client_code"]):
        customer = ClientData.valid_customer()

    clients.add_customer(customer)

    assert clients.is_customer_saved_successfully()

    clients.search_client(
        customer["client_code"]
    )

    assert clients.verify_client_name_exists(
        customer["client_code"]
    )

    clients.clear_search()

    assert clients.is_search_box_empty()

    page.wait_for_timeout(1000)

    assert clients.get_total_customer_count() == initial_count + 1

    print(f"{clients.get_total_customer_count()} and Initial count with newly added device : {initial_count + 1}")