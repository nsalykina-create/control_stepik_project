from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def solve_quiz(self):
        self.solve_quiz_and_get_code()

    def compare_name_book(self):
        name_books = self.browser.find_element(*ProductPageLocators.NAME_BOOK)
        name = name_books.text
        name_book_in_basket = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_BASKET)
        name1 = name_book_in_basket.text
        assert name == name1, 'Имя книги не совпадает в корзине'

    def compare_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        summa = price.text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        summa1 = price_in_basket.text
        assert summa == summa1, 'Цена не совпадает в корзине'
