from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base

class Client_information_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    confirmation_button = "[data-save-button='true']"

    # Getters
    def get_confirmation_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.confirmation_button)))

    # Actions
    def click_confirmation_button(self):
        self.get_confirmation_button().click()

    # Methods
    def final_order(self):
        self.move_to_coords_on_page(0, 1600)
        self.click_confirmation_button()