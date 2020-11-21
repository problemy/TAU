import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
logger = logging.getLogger('Test2_2logger')
logging.basicConfig(filename="Test2_2.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Edge(executable_path=r'C:\Users\matko\PycharmProjects\pythonTests\msedgedriver.exe')
logger.info('Wchodzę na stronę logowania')
driver.get("https://simteq.pl/do/login?referer=https://simteq.pl/index.jsp")
driver.maximize_window()
logger.info('Uzupełniam login')
temp = driver.find_element_by_id("email")
temp.click()
temp.send_keys("hivaseh648@1981pc.com")
logger.info('Uzupełniam hasło')
temp= driver.find_element_by_id("password")
temp.click()
temp.send_keys("test123")
logger.info('Wysyłam formularz logowania')
temp = driver.find_element_by_class_name("btn.btn-primary")
temp.click()
logger.info('Przechodzę do koszyka')
driver.get("https://simteq.pl/do/cart")
logger.info('Usuwam przedmiot z koszyka')
temp = driver.find_element_by_class_name("del-goods")
temp.click()


driver.close()