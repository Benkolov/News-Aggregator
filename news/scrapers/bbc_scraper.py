from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_scraper import BaseScraper


class BBCScraper(BaseScraper):
    def parse(self):
        self.load_page()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sc-93223220-0"))
        )

        articles = self.driver.find_elements(By.CLASS_NAME, "sc-93223220-0")
        data = []

        for article in articles:
            try:
                title_elem = article.find_element(By.CSS_SELECTOR, '[data-testid="card-headline"]')
                title = title_elem.text.strip()
            except Exception as e:
                title = ""
            try:
                link_elem = article.find_element(By.TAG_NAME, 'a')
                link = link_elem.get_attribute('href')
            except Exception as e:
                link = ""

            try:
                image_elem = article.find_element(By.TAG_NAME, 'img')
                image = image_elem.get_attribute('src')
            except Exception as e:
                image = ""

            self.save_article(title, link, image)
            data.append({"title": title, "url": link, "image": image})

        return data
