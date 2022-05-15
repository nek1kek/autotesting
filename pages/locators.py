from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#username")
    PASSWORD_FORM = (By.CSS_SELECTOR, "#password")
    BUTTON_SUBMIT = (By.XPATH, "//*[@id=\"login-form\"]/div[3]/button")
    FORGET_PASSWORD_FORM = (By.XPATH, "//*[@id=\"login-form\"]/div[3]/div[1]/div[2]/a")
    REGISTRATION_FORM = (By.XPATH, "//*[@id=\"login-form\"]/div[3]/div[1]/div[1]/a")


class ForgottenPageLocators():
    RECOVERY_FORM = (By.XPATH, "/ html / body / div / div / form / div[2] / input")


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "/html/body/div/div[2]/div/div/form")
    TIMETABLE = (By.XPATH, "/html/body/div/div[3]/a")
    RECORDINGS_VIDEO = (By.XPATH, "//*[@id=\"page-content-wrapper\"]/div/div/div[1]/a[1]")
    MESS_LINK = (By.XPATH, "/html/body/div[3]/aside/ul/li[3]/a")
    NEW_MESS = (By.XPATH, "//*[@id=\"page-content-wrapper\"]/div/h1/a")
    SEND = (By.XPATH, "//*[@id=\"new_talk\"]/div[4]/div[2]/div[3]/button")
    ERRMESS = (By.XPATH, "//*[@id=\"page-content-wrapper\"]/div/div[1]")
    COURSE = (By.XPATH, "//*[@id=\"page-content-wrapper\"]/div/div/div[1]/a[4]")
    INFO = (By.CSS_SELECTOR, "#page-content-wrapper > div > h2 > button")
    OUT = (By.XPATH, "//*[@id=\"wrapper\"]/nav/div/ul/li[2]/a")
    OUT_BUTTON = (By.XPATH, "//*[@id=\"wrapper\"]/nav/div/ul/li[2]/ul/li/a")
    SIDEBAR = (By.CSS_SELECTOR, "#sidebar-toggle > i")
    FIND_ME = (By.XPATH, "//*[@id=\"new_talk\"]/div[4]/div[2]/div[3]/button")
