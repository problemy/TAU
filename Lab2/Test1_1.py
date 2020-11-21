import time
import logging
from selenium import webdriver

logger = logging.getLogger('Test1_1logger')
logging.basicConfig(filename="Test1_1.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)



driver = webdriver.Chrome(executable_path=r'C:\Users\matko\PycharmProjects\pythonTests\drivers\chromedriver.exe')
driver.maximize_window()

logger.info('Wchodzę na stronę poradykomputerowe')
driver.get("http://www.poradykomputerowe.pl/")

logger.info('Akceptacje cookiec')
cookies = driver.find_element_by_class_name("submit-cookie")
cookies.click()
logger.info('Wchodzę na stronę rejestracji')
register = driver.find_element_by_link_text("rejestracja")
register.click()
logger.info('Uzupełniam e-mail działający jako login')
time.sleep(1)
email = driver.find_element_by_id("RegForm_email")
email.click()
email.send_keys("mail@mail.pl")
logger.info('Uzupełniam hasło')
password = driver.find_element_by_id("RegForm_password_reg")

password.click()
password.send_keys("Q1w@e3r4")
logger.info('Potwierdzam hasło')
password2 = driver.find_element_by_id("RegForm_password_again")
password2.click()
password2.send_keys("Q1w@e3r4")
logger.info('Akceptuję regulamin')
checkbox = driver.find_element_by_id("RegForm_checkboxes1")
checkbox.click()
logger.info('Wysyłam formularz')
registerSubmit = driver.find_element_by_name("yt0")
registerSubmit.click()



driver.close()
