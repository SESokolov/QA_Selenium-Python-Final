from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):
    def add_product_to_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()
        self.solve_quiz_and_get_code()
        print(f"Product {book_name} add to basket, price {book_price}")
        book_price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET).text
        book_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        print(f"Product {book_name_basket} in basket, price in basket is {book_price_basket}")
        assert book_name == book_name_basket, "Product name in product page and product name in basket didn`t match"
        assert book_price == book_price_basket, "Product price in product page and product price in basket didn`t match"

    #простое добавление товара в корзину без проверки и вычисления кода
    def add_product_to_basket_without_code(self):
        WebDriverWait(self.browser, 5).until(
            ec.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET)).click()

    #проверяет, что элемент не появляется на странице в течение заданного времени (упадет, как только увидит искомый элемент)
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
    
        return False

    #проверяет исчезнет ли элемент в тчение заданного времени (будет ждать до тех пор, пока элемент не исчезнет)
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
    
        return True
