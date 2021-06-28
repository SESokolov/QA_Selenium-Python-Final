# Базовяа страница, от которой будут унаследованы все остальные классы. В ней мы опишем вспомогательные методы для работы с драйвером.
import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
#        self.browser.implicitly_wait(timeout) # для задания 4.3.6 необходимо закомментировать

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK) # LOGIN_LINK_INVALID, для 4.3.13 опставил LOGIN_LINK
        link.click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
