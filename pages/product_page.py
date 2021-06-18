import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ProductPage(BasePage):
    def add_product_to_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()
        self.solve_quiz_and_get_code()
        print(f"Product {book_name} add to basket, price {book_price}")
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.BASKET_LINK)).click()
        book_price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET).text
        book_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        print(f"Product {book_name_basket} in basket, price in basket is {book_price_basket}")
        assert book_name == book_name_basket, "Product name in product page and product name in basket didn`t match"
        assert book_price == book_price_basket, "Product price in product page and product price in basket didn`t match"
#        time.sleep(20)