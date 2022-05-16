from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage():
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.RECORDINGS_VIDEO), "rECORDING_VIDEO icon is not presented," \
                                                                            " probably unauthorised user"

    def should_not_be_authorized_user(self):
        assert self.is_not_element_present(*BasePageLocators.RECORDINGS_VIDEO), "rECORDING_VIDEO icon is not presented," \
                                                                                " probably unauthorised user"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link should be present"

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):  # есть ли элемент на странице
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):  # нету ли элемента на странице
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_message(self):
        mess_link = self.browser.find_element(*BasePageLocators.MESS_LINK)
        mess_link.click()

    def go_to_courses(self):
        courses = self.browser.find_element(*BasePageLocators.COURSE)
        courses.click()

    def log_out(self):
        button = self.browser.find_element(*BasePageLocators.OUT)
        button.click()
        button = self.browser.find_element(*BasePageLocators.OUT_BUTTON)
        button.click()

    def should_be_send_mess(self):
        assert self.is_element_present(*BasePageLocators.NEW_MESS), "New message button is not presented"

    def try_send_empty_mess(self):
        mess = self.browser.find_element(*BasePageLocators.NEW_MESS)
        mess.click()
        send_button = self.browser.find_element(*BasePageLocators.SEND)
        send_button.click()
        assert self.is_element_present(*BasePageLocators.ERRMESS), "Error message is not presented"

    def should_be_info(self):
        assert self.is_element_present(*BasePageLocators.INFO), "Info in not present"

    def should_not_be_button(self):
        bar = self.browser.find_element(*BasePageLocators.SIDEBAR)
        bar.click()
        assert self.is_not_element_present(
            *BasePageLocators.FIND_ME), "Side panel didn't disappear after clicking bar button"
