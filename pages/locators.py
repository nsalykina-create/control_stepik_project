from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@type='submit' and @class='btn btn-lg btn-primary btn-add-to-basket']")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    NAME_BOOK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    NAME_BOOK_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE_IN_BASKET =(By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class MainPageLocators():
    GO_TO_BASKET = (By.XPATH, "//a[@class='btn btn-default']")

class BasePageLocators():
    BASKET_IS_NULL = (By.TAG_NAME, "p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS_LOCATOR = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_SUBMIT = (By.NAME, "login_submit")
    REG_EMAIL_LOCATOR = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS1_LOCATOR = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASS2_LOCATOR = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")


