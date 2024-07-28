from playwright.sync_api import Page
from . import LoginPageLocators


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = LoginPageLocators.USER_NAME_INPUT
        self.password_input = LoginPageLocators.PASSWORD_INPUT
        self.login_button = LoginPageLocators.LOGIN
        self.org_select = LoginPageLocators.ORG_SELECT

    def enter_username(self, username: str):
        self.page.fill(self.username_input, username)

    def enter_password(self, password: str):
        self.page.fill(self.password_input, password)

    def click_login(self):
        self.page.click(self.login_button)

    def select_firm(self, firm_name: str):
        self.page.wait_for_selector(self.org_select)
        self.page.select_option(self.org_select, label=firm_name)
