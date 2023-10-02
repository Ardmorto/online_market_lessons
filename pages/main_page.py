from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Main_page(Base):
    main_page_url = 'https://zebrazoo.ru/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    dog_catalog = '//*[@id="bx_1847241719_141"]/a[2]'
    dog_catalog_treats = '//*[@id="bx_1847241719_148"]/a/span'
    filter_by_names = "//span[.='по имени']"
    select_product_1 = ".js-buyform20128 .b-pay__add2basket"
    cart = ".basket.tpanel__block .hidden-xs"


    #Getters
    def get_dog_catalog_menu(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.dog_catalog)))
    def get_dog_catalog_treats_menu(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.dog_catalog_treats)))
    def get_filter_by_name_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.filter_by_names)))
    def get_select_product(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_product_1)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart)))

    #Actions
    def go_to_main_page(self):
        self.driver.get(self.main_page_url)

    def click_dog_catalog_menu(self):
        self.get_dog_catalog_menu().click()

    def click_dog_catalog_treats_menu(self):
        self.get_dog_catalog_treats_menu().click()

    def click_filter_by_names(self):
        self.get_filter_by_name_button().click()

    def click_select_product(self):
        self.get_select_product().click()

    def click_cart_button(self):
        self.get_cart_button().click()

    #Methods
    def select_product(self):
        self.go_to_main_page()
        self.click_dog_catalog_menu()
        self.click_dog_catalog_treats_menu()
        self.click_filter_by_names()
        self.click_select_product()
        self.move_to_element_on_page(self.get_cart_button())
        self.click_cart_button()