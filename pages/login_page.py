import env
from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.enter_user(login=env.LOGIN, password=env.PASSWORD)

    def forget_password(self):
        forget_password_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        forget_password_form.click()

    def input_mail(self):
        email = str(time.time()) + "@fakemail.org"
        email_input = self.browser.find_element(*LoginPageLocators.RECOVERY_FORM)
        email_input.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.ASSERT_VIEW), "Login form should be not present"

    def should_be_forgotten(self):
        assert "forgotten" in self.browser.current_url, "'forgotten' should be in current url"

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' should be in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form should be not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Register form should be present"

    def enter_user(self, login=env.LOGIN, password=env.PASSWORD):
        login_input = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        login_input.send_keys(login)
        password_input.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT)
        button_submit.click()
