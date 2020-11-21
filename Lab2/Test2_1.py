import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
logger = logging.getLogger('Test2_1logger')
logger.setLevel(logging.INFO)
logging.basicConfig(filename="Test2_1.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)



driver = webdriver.Edge(executable_path=r'C:\Users\matko\PycharmProjects\pythonTests\drivers\msedgedriver.exe')
logger.info('Wchodzę na stronę logowania simteq')
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
logger.info('Przechodzę na kategorię prawdziwe okazje')
temp = driver.find_element_by_partial_link_text("Prawdziwe Okazje !")
temp.click()
#temp = driver.find_element_by_partial_link_text("do/item/063780/Klej-Verano-do-montazu-folii-310ml-biel")

#temp = driver.find_element_by_xpath("do/item/063780/Klej-Verano-do-montazu-folii-310ml-biel")
logger.info('Wchodzę w stronę interesującego mnie przedmiotu ze sklepu')
temp = driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div[2]/div[4]/div[7]/div/div[1]/a')
temp.click()
logger.info('Dodaję przedmiot do koszyka')
temp = driver.find_element_by_class_name("btn.btn-primary.col-xs-8")
temp.click()
logger.info('Przechodzę na stronę koszyka')
driver.get("https://simteq.pl/do/cart")

cart_item = driver.find_element_by_class_name('col-sm-5.cart-title')

assert cart_item.text == "PRODUKT"

driver.close()