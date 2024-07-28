class ClientsPageLocators:
    ADVISORS = "xpath=//label[normalize-space()='Advisors:']"
    ADD_NEW_CLIENT = "xpath=//button[@id='addNewClientBtnId']"


class LoginPageLocators:
    USER_NAME_INPUT = '#loginEmail'
    PASSWORD_INPUT = '#loginPassword'
    LOGIN = "xpath=//button[@type='submit']"
    ORG_SELECT = '#orgId'


class NewClientPageLocators:
    TITLE = "xpath=//h3[normalize-space()='Add new client']"
    FIRST_NAME = "xpath=//span[normalize-space()='First name:']"
    LAST_NAME = "xpath=//span[normalize-space()='Last name:']"
    ADD_CLIENT_BUTTON = '#save-client-changes-btn'
