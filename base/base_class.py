from datetime import datetime
from selenium.webdriver import ActionChains

class Base():
    def __init__(self, driver):
        self.driver = driver

    #Methods
    def get_curret_url(self): #Получение текущей ссылки
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    def assert_word(self, word, result): #Парсинг слова на странице
        assert word.text == result

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result

    def move_to_element_on_page(self, element): #переход к элементу по его локатору
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def move_to_coords_on_page(self, x, y): #Произвольный переход по координатам на странице
        self.driver.execute_script(f'window.scrollTo({x}, {y})')

    def take_screenshot(self):
        now_date = datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        screenshot_name = f'Screenshot {now_date}.png'
        self.driver.save_screenshot(f'C:\\Users\\Ardmorto\\PycharmProjects\\online_market_lessons\\screen\\{screenshot_name}')