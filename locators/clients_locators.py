class ClientsLocators:

    CLIENTS_MENU = "#side-menu-customers"

    CLIENT_HEADER = "h4:has-text('Clients')"

    CLIENT_ROWS = "tbody tr"

    NEXT_BUTTON = "#next-btn"

    PREVIOUS_BUTTON = "#back-btn" 

    ADD_CUSTOMER_BUTTON = "#admin-customer-add-customer-btn"

    ADD_CUSTOMER_DIALOG = "h2:has-text('Add New Client')"


    ORGANISATION_NAME = "#admin-customer-organisation-name"

    CLIENT_CODE = "#admin-client-code"

    SCHOOL_DISTRICT = "#admin-school-district"
    
    DISTRICT_PREFIX = "#admin-district-code"

    COUNTRY = "#admin-customer-country"

    STATE = "#admin-customer-state"

    CITY = "#admin-customer-city"

    ADDRESS = "#admin-customer-address"

    CUSTOMER_CONTACT = "#admin-customer-contact"

    EMAIL = "#admin-customer-email"

    PHONE = "#admin-customer-phone"

    SAVE_BUTTON = "#admin-customer-save-btn"

    CANCEL_BUTTON = "#admin-customer-close-btn"  

    YES_BUTTON = "#ok-btn" 

    # Validation Messages

    ORGANISATION_NAME_REQUIRED = "#admin-customer-organisation-name-helper-text"

    COUNTRY_REQUIRED = "#admin-customer-country-helper-text"

    STATE_REQUIRED = "#admin-customer-state-helper-text"

    CITY_REQUIRED = "#admin-customer-city-helper-text"

    CLIENT_CODE_REQUIRED = "#admin-client-code-helper-text"

    CUSTOMER_CONTACT_REQUIRED = "#admin-customer-contact-helper-text"

    EMAIL_REQUIRED = "#admin-customer-email-helper-text"

    PHONE_REQUIRED = "#admin-customer-phone-helper-text" 

    CUSTOMER_SAVE_SUCCESS_MESSAGE = "//p[text()='Successfully saved!']" 

    CUSTOMER_DELETE_SUCCESS_MESSAGE = "//p[text()='Successfully deleted!']"

    SEARCH_CLIENT = "#admin-customer-search-filter"

    CLIENT_CODE_UNIQUE_MESSAGE = "//p[text()='code must be unique']"

    EDIT_CLIENT_BUTTON = "#admin-customer-update-customer-btn"

    EDIT_BACK_BUTTON = "#customers-back-link"
    
    UPDATE_CLIENT_BUTTON = "#admin-customer-save-btn"

    # MORE_ACTIONS_BUTTON = "[data-testid='MoreHorizIcon']"

    DELETE_BUTTON = "text=Delete"

    DELETE_CONFIRMATION_DIALOG = "#alert-dialog-title"

    DELETE_CONFIRM_BUTTON = "#ok-btn"

    DELETE_CANCEL_BUTTON = "#cancel-btn"

    NO_DATA_FOUND = "td[colspan='10']"

    PAGINATION_COUNT = ".MuiGrid-root.css-rfnosa p"

    CLIENT_FILTER = "#admin-system-customer-filter"

    VARIANT_FILTER = "#admin-product-subtypes-filter"