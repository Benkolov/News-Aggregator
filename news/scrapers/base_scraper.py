from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from news.models import Headline


class BaseScraper:
    def __init__(self, url, source_name):
        self.url = url
        self.source_name = source_name
        self.driver = self.init_driver()

    def init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--enable-javascript")

        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def load_page(self):
        self.driver.get(self.url)

        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )

    def save_article(self, title, link, image):
        if title and not Headline.objects.filter(title=title, url=link).exists():
            Headline.objects.create(
                title=title, 
                url=link, 
                image=image,
                source=self.source_name
            )

    def parse(self):
        raise NotImplementedError()

    def close(self):
        self.driver.quit()
