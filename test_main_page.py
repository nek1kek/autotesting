import time
import env
from pages.main_page import MainPage
from pages.login_page import LoginPage

"""
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page=BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.text_basket_is_empty_should_be_present()
"""


class TestLoginFromMainPage():
    def test_can_enter_with_login_page(self, browser):  # РАБОТАЕТ!
        link = "https://home.mephi.ru/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_wrong_enter(self, browser):
        link = "https://auth.mephi.ru/login?service=https%3A%2F%2Fhome.mephi.ru%2Fhome"
        register_page = LoginPage(browser, link)
        register_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "kdoemo38hedk84"
        register_page.enter_user(email, password)
        register_page.should_not_be_authorized_user()

    def test_forget_password(self, browser):
        link = "https://auth.mephi.ru/login?service=https%3A%2F%2Fhome.mephi.ru%2Fhome"
        register_page = LoginPage(browser, link)
        register_page.open()
        register_page.forget_password()
        register_page.should_be_forgotten()

    def test_send_message(self, browser):
        link = "https://auth.mephi.ru/login?service=https%3A%2F%2Fhome.mephi.ru%2Fhome"
        home_page = LoginPage(browser, link)
        home_page.open()
        home_page.enter_user(login=env.LOGIN, password=env.PASSWORD)
        home_page.go_to_message()
        home_page.should_be_send_mess()

    def test_send_empty_mess(self, browser):
        link = "https://auth.mephi.ru/login?service=https%3A%2F%2Fhome.mephi.ru%2Fhome"
        bpage = LoginPage(browser, link)
        bpage.open()
        bpage.enter_user(login=env.LOGIN, password=env.PASSWORD)
        bpage.go_to_message()
        bpage.try_send_empty_mess()

    def test_info_button(self, browser):
        link = "https://auth.mephi.ru/login?service=https%3A%2F%2Fhome.mephi.ru%2Fhome"
        page = LoginPage(browser, link)
        page.open()
        page.enter_user()
        page.go_to_courses()
        page.should_be_info()

    def test_info_button(self, browser):
        link = "https://auth.mephi.ru/login?service=https%3A%2F%2Fhome.mephi.ru%2Fhome"
        page = LoginPage(browser, link)
        page.open()
        page.enter_user()
        page.go_to_courses()
        page.should_be_info()

    def test_enter_out(self, browser):
        link = "https://auth.mephi.ru/login?service=https%3A%2F%2Fhome.mephi.ru%2Fhome"
        page = LoginPage(browser, link)
        page.open()
        page.enter_user()
        page.log_out()
        page.should_be_login_link()

    def test_sidebar(self, browser):
        link = "https://auth.mephi.ru/login?service=https%3A%2F%2Fhome.mephi.ru%2Fhome"
        page = LoginPage(browser, link)
        page.open()
        page.enter_user()
        page.should_not_be_button()
