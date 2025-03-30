from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_scraper import BaseScraper
import time
import requests
from bs4 import BeautifulSoup


class DnevnikScraper(BaseScraper):
    def parse(self):
        self.load_page()
        time.sleep(3)
        data = []
        headlines = self.driver.find_elements(By.CSS_SELECTOR, "h3 a")
        urls = []
        titles = {}
        
        for index, headline in enumerate(headlines[:6]):
            try:
                url = headline.get_attribute('href')
                title = headline.get_attribute('textContent').strip()
                
                if not title:
                    title = headline.text.strip()
                
                urls.append(url)
                titles[url] = title
            except Exception:
                continue
        
        for url in urls:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                title = titles.get(url, "")
                image_element = soup.select_one('figure img')
                image = image_element.get('src') if image_element else ""

                if title and url:
                    self.save_article(title, url, image)
                    data.append({"title": title, "url": url, "image": image})
            except Exception:
                continue
        
        return data
