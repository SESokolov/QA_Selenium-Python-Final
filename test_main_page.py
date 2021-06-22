import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        self.page.open()                      # открываем страницу
        self.page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_page()
    
    def test_guest_should_see_login_link(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.should_be_login_link()

@pytest.mark.test4310
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_basket_page()         # выполняем метод страницы — переходим на страницу корзины
    assert page.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Basket is not empty"
    assert page.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Not found text 'Basket is empty'"