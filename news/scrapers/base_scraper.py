from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from news.models import Headline


class BaseScraper:
    def __init__(self, url):
        self.url = url
        self.driver = self.init_driver()

    def init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")

        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def load_page(self):
        self.driver.get(self.url)

    def save_article(self, title, link, image):

        if title and not Headline.objects.filter(title=title, url=link).exists():
            Headline.objects.create(title=title, url=link, image=image)

    def parse(self):
        raise NotImplementedError()

    def close(self):
        self.driver.quit()
