from .base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class GongScraper(BaseScraper):
    def parse(self):
        driver = self.driver
        headlines_data = []
        try:
            self.load_page()
            news_elements = driver.find_elements(By.CSS_SELECTOR, 'div[class^="card-"]')

            for element in news_elements:
                try:
                    link_element = element.find_element(By.CSS_SELECTOR, 'div.img-wrap > a')
                    url = link_element.get_attribute('href')
                    title = link_element.get_attribute('title')
                    img_element = link_element.find_element(By.TAG_NAME, 'img')
                    image_url = img_element.get_attribute('src')

                    if url and title and image_url:
                        self.save_article(title.strip(), url, image_url)
                        headlines_data.append({
                            'title': title.strip(),
                            'url': url,
                            'image': image_url
                        })

                except NoSuchElementException:
                    pass
                except Exception:
                    continue

        except TimeoutException:
            pass
        except Exception:
            pass

        return headlines_data
