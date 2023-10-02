from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class User_profile_page(Base):
    profile_page_url = 'https://zebrazoo.ru/personal/profile/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    current_orders_menu_button = "//h2[contains(.,'Текущие заказы')]"
    cancel_order_button = ".sale-order-list-cancel-link"
    reason_field = "[name='REASON_CANCELED']"
    confirm_cancle_button = "[name='action']"

    # Getters
    def get_current_orders_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.current_orders_menu_button)))

    def get_cancle_order_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cancel_order_button)))

    def get_reason_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.reason_field)))

    def get_confirm_cancle_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.confirm_cancle_button)))

    # Actions
    def go_to_user_profile_page(self):
        self.driver.get(self.profile_page_url)

    def click_current_orders_button(self):
        self.get_current_orders_button().click()

    def click_cancle_order_button(self):
        self.get_cancle_order_button().click()

    def input_reason_field(self, reason):
        self.get_reason_field().send_keys(reason)

    def click_confirm_cancle_button(self):
        self.get_confirm_cancle_button().click()

    # Methods
    def cancle_last_order(self):
        self.go_to_user_profile_page()
        self.click_current_orders_button()
        self.click_cancle_order_button()
        self.input_reason_field('Test')
        self.click_confirm_cancle_button()