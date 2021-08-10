from .pages.product_page import ProductPage
import time
import pytest
from .pages.base_page import BasePage

okay_link = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

bugged_link = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"]
@pytest.mark.parametrize('link', [["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"]])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser,link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product()
    time.sleep(1)
    page.solve_quiz()
    time.sleep(1)
    page.compare_name_book()
    page.compare_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product()
    time.sleep(1)
    page.should_dissapear_of_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_basket_from_main_page()
    time.sleep(1)
    page.basket_is_null()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.email = str(time.time()) + "@fakemail.org"
        self.link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = ProductPage(self.browser,
                           self.link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        self.passw = "passWORD"
        page.register_new_user(email, passw)
        page.login(email, passw)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser, link):
        # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_product()
        time.sleep(1)
        page.solve_quiz()
        time.sleep(1)
        page.compare_name_book()
        page.compare_price()


    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_not_be_success_message()



