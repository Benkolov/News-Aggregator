from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ако не искаш да се показва браузъра
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

service = Service()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.sega.bg')  # Тествай с конкретен сайт

# Примерно изчакване, за да видиш как се зарежда страницата
driver.implicitly_wait(10)

print(driver.title)
driver.quit()
