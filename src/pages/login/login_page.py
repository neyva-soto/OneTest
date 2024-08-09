from src.pages.base_page import BasePage
from src.pages.login.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def login_button_click(self):
        loop = self.context.async_context.loop
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        loop.run_until_complete(login_button.click())
        return login_button

    def get_summary_text(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.find_element(LoginPageLocators.SUMMARY).inner_text())


    def set_search_user_input(self, search_input):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.type(LoginPageLocators.USERNAME_INPUT, search_input))

    def set_search_pass_input(self, search_input):
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.type(LoginPageLocators.PASSWORD_INPUT, search_input))

    def get_dashboard_text(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.find_element(LoginPageLocators.DASHBOARD_TITLE).inner_text())

    def open(self):
        application_url = self.context.config.userdata.get("applicationUrl",
                                                      "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        loop = self.context.async_context.loop
        loop.run_until_complete(self.context.page.goto(application_url))

    def verify_input_field(self, input_name):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(f'input[name="{input_name}"]'))

    def verifyUserInputRequired(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.WARNIG_USER_INPUT))

    def verifyPasswordInputRequired(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.WARNIG_PASSWORD_INPUT))

    def verifydisplayButton(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.LOGIN_BUTTON))

    def verifydisplaywarnin(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.INVALID_CREDENTIAL))

    def verifyForgotPassword(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.FORGOT_PASSWORD))

    def verifyFormForgotPassword(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.FORM_FORGOT))

    def verifyFieldPassword(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.FIELD_PASSWORD))

    def click_link_orange(self):
        loop = self.context.async_context.loop
        link_orange = self.find_element(LoginPageLocators.LINK_ORANGE)
        print(link_orange)
        loop.run_until_complete(link_orange.click())
        return link_orange

    def verifyPageOrange(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.PAGE_ORANGE))

    def verifyEmptySpace(self):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.query_selector(LoginPageLocators.LOGIN_BUTTON))

    def getInputText(self, locator):
        loop = self.context.async_context.loop
        return loop.run_until_complete(self.context.page.locator(locator).input_value())


