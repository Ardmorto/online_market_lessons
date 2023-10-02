import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.user_profile_page import User_profile_page
from base.base_class import Base

def test_full_path(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Driver manipulations
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    #variables
    base = Base(driver)
    login = Login_page(driver)
    main_page = Main_page(driver)
    cart_page = Cart_page(driver)
    client_page = Client_information_page(driver)
    user_profile = User_profile_page(driver)

    #Main actions
    login.authorization()
    main_page.select_product()
    cart_page.product_confirmation()
    client_page.final_order()
    time.sleep(2)
    base.assert_url('https://zebrazoo-ab.server.paykeeper.ru/create/')
    base.take_screenshot()
    driver.back()
    user_profile.cancle_last_order()