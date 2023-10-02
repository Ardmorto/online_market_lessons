from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Cart_page(Base):
    cart_page_url = 'https://zebrazoo.ru/personal/cart/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    order_button = ".btn"
    delete_product_button = "//span[@class='basket-item-actions-remove']"

    # Getters
    def get_order_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.order_button)))

    def get_delete_button(self):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, self.delete_product_button)))

    # Actions
    def click_order_button(self):
        self.get_order_button().click()

    def click_delete_button(self):
        self.get_delete_button().click()

    # Methods
    def delete_old_products(self):
        self.driver.get(self.cart_page_url)
        self.click_delete_button()

    def product_confirmation(self):
        self.click_order_button()