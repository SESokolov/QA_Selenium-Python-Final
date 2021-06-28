from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "login"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")
    PRODUCT_NAME_BASKET = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alertinner>p>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, ".basket-title") # если найден, то корзина не пустая
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p") # текст, что корзина пустая