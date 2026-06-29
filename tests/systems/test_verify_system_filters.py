from pages.login_page import LoginPage
from pages.systems_page import SystemsPage
from utils.config_reader import ConfigReader


def test_verify_system_filters(page):

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
    
    assert systems.enable_all_columns()

    # Verify Client Filter

    assert systems.select_client(
        "EconQA2"
    ), "Failed to select Client."

    assert systems.verify_client_filter(
        "EconQA2"
    ), "Client filter verification failed."

    assert systems.clear_client_filter(), \
        "Failed to clear Client filter."

    # Verify Variant Filter

    assert systems.select_variant(
        "VEM V1"
    ), "Failed to select Variant."

    assert systems.verify_variant_filter(
        "VEM V1"
    ), "Variant filter verification failed."

    assert systems.clear_variant_filter(), \
        "Failed to clear Variant filter."