from selenium.webdriver.common.by import By
from .base_scraper import BaseScraper
import time


class BBCScraper(BaseScraper):
    def parse(self):
        self.load_page()
        time.sleep(3)
        
        data = []
        articles = self.driver.find_elements(By.CSS_SELECTOR, "div[data-testid$='-card']")
        
        for index, article in enumerate(articles[:6]):
            try:
                try:
                    title_element = article.find_element(By.CSS_SELECTOR, '[data-testid="card-headline"]')
                    title = title_element.text.strip()
                except Exception:
                    title = ""
                
                try:
                    link_element = article.find_element(By.TAG_NAME, 'a')
                    link = link_element.get_attribute('href')
                    
                    if link and not link.startswith(('http', 'https')):
                        link = f"https://www.bbc.com{link}"
                except Exception:
                    link = ""
                
                try:
                    image_element = article.find_element(By.TAG_NAME, 'img')
                    image = image_element.get_attribute('src')
                    
                    if not image and image_element.get_attribute('srcset'):
                        srcset_parts = image_element.get_attribute('srcset').split(',')
                        image = srcset_parts[0].strip().split(' ')[0]
                except Exception:
                    image = ""
                
                if title and link:
                    self.save_article(title, link, image)
                    data.append({"title": title, "url": link, "image": image})
            except Exception:
                continue
        
        return data
