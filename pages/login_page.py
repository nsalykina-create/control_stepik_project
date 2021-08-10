from .base_page import BasePage
from .main_page import MainPage
from selenium import webdriver
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        links = browser.current_url
        assert links == "http://selenium1py.pythonanywhere.com/accounts/login/", "Login url is not correct"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        try:
            self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_LOCATOR)
            self.is_element_present(*LoginPageLocators.LOGIN_PASS_LOCATOR)
            self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT)
            flag = 1
        except:
            flag = 0
        assert flag == 1, "Login form is not correct"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        try:
            self.is_element_present(*LoginPageLocators.REG_EMAIL_LOCATOR)
            self.is_element_present(*LoginPageLocators.REG_PASS1_LOCATOR)
            self.is_element_present(*LoginPageLocators.REG_PASS2_LOCATOR)
            self.is_element_present(*LoginPageLocators.REG_SUBMIT)
            flg = 1
        except:
            flg = 0
        assert flg == 1, "Login form is not correct"

    def register_new_user(self, email, password):
        em = self.browser.find_element(*LoginPageLocators.REG_EMAIL_LOCATOR)
        em.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS1_LOCATOR)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS2_LOCATOR)
        pass2.send_keys(password)
        sub = self.browser.find_element(*LoginPageLocators.REG_SUBMIT)
        sub.click()

    def login_user(self, email, password):
       em1 =  self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_LOCATOR)
       em1.send_keys(email)
       pas1 =self.browser.find_element(*LoginPageLocators.LOGIN_PASS_LOCATOR)
       pas1.send_keys(password)
       button = self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT)
       button.click()