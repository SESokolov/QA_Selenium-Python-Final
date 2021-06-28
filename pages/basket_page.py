from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def should_be_message_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Not found text 'Basket is empty'"

    #проверяет, что элемент не появляется на странице в течение заданного времени (упадет, как только увидит искомый элемент)
    def should_not_be_items_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket is not empty"
