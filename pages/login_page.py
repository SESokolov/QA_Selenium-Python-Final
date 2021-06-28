from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # проверка на корректный url адрес
    def should_be_login_url(self):
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, f"'{LoginPageLocators.LOGIN_URL}' not in current url"
        assert True

    # проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    # проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True
    # регистрация нового пользователя
    def register_new_user(self, email, password):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL), "E-mail input field not found"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1), "Password input field not found"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2), "Confirm password input field not found"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT), "Register button not found"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT).click()