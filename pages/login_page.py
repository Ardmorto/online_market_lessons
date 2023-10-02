from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Login_page(Base):
    auth_url = 'https://zebrazoo.ru/auth/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    login_field = '//input[@name="USER_LOGIN"]'
    password_field = '//input[@name="USER_PASSWORD"]'
    login_button = '//button[@name="Login"]'
    main_word = '//h1[@class="pagetitle"]'

    #Getters
    def get_email_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.login_field)))
    def get_password_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))
    def get_login_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    def get_main_word(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.main_word)))

    #Actions
    def input_user_name(self, user_name):
        self.get_email_field().send_keys(user_name)

    def input_password(self, password):
        self.get_password_field().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    #Methods
    def authorization(self):
        self.driver.get(self.auth_url)
        self.driver.maximize_window()
        self.input_user_name('Ardmorto')
        self.input_password('password_for_test')
        self.click_login_button()
        self.assert_word(self.get_main_word(), 'АВТОРИЗАЦИЯ')