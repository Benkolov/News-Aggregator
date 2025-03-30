from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from news.scrapers.base_scraper import BaseScraper


class WebcafeScraper(BaseScraper):
    def parse(self):
        self.load_page()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "article"))
        )
        articles = self.driver.find_elements(By.CLASS_NAME, "article")[:6]

        data = []

        for article in articles:
            title = article.text.strip()
            link = article.find_element(By.TAG_NAME, 'a').get_attribute('href') if article.find_elements(By.TAG_NAME,
                                                                                                         'a') else ''
            image = article.find_element(By.TAG_NAME, 'img').get_attribute('src') if article.find_elements(By.TAG_NAME,
                                                                                                           'img') else ''
            self.save_article(title, link, image)

            data.append({"title": title, "url": link, "image": image})

        return data
