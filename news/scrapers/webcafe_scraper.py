from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

from news.scrapers.base_scraper import BaseScraper


class WebcafeScraper(BaseScraper):
    def parse(self):
        self.load_page()
        data = []

        # Wait for the page to load completely
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "skeleton-left"))
        )

        # Add a small delay to ensure all elements are loaded
        time.sleep(2)

        # Print page title for debugging
        print(f"Page title: {self.driver.title}")

        # Simplified approach: Get 6 articles only from global-leading-articles-big
        try:
            # Find the global-leading-articles-big container
            big_articles_container = self.driver.find_element(By.CLASS_NAME, "global-leading-articles-big")

            # Find all article elements inside this container
            articles = big_articles_container.find_elements(By.CLASS_NAME, "article")
            print(f"Found {len(articles)} articles in global-leading-articles-big")

            # Process up to 6 articles
            for article in articles[:6]:
                try:
                    # Print article HTML for debugging
                    article_html = article.get_attribute('outerHTML')
                    print(f"Article HTML: {article_html[:100]}...")

                    # Get the content div which contains the title, link and image
                    content_div = article.find_element(By.CLASS_NAME, "content")
                    print("Found content div")

                    # Get the description div which contains the title
                    description_div = content_div.find_element(By.CLASS_NAME, "description")
                    print("Found description div")

                    # Get the title and link from h2 > a
                    title_element = description_div.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
                    title = title_element.text.strip()
                    # If title is empty, try to get it from the title attribute
                    if not title:
                        title = title_element.get_attribute('title') or ""
                    # If still empty, try to get it from the inner HTML
                    if not title:
                        title = title_element.get_attribute('innerHTML').strip()
                    link = title_element.get_attribute('href')
                    print(f"Found title: '{title[:30]}...' and link: {link}")

                    # Get the image from the image div
                    image_div = content_div.find_element(By.CLASS_NAME, "image")
                    image = image_div.find_element(By.TAG_NAME, "img").get_attribute('src')
                    print(f"Found image: {image}")

                    # Skip articles from "Оня, дето не го трият" section
                    if "onya-deto-ne-go-triyat" in link:
                        print(f"Skipping article from 'Оня, дето не го трият' section: {title[:50]}...")
                        continue

                    # Skip invalid URLs (like anchors or homepage links)
                    if link.endswith("#") or link == "https://webcafe.bg/" or link == "https://www.webcafe.bg/":
                        print(f"Skipping article with invalid URL: {link}")
                        continue

                    # Save the article (we already checked that title, link and image exist)
                    print(f"Saving article: {title[:50]}...")
                    self.save_article(title, link, image)
                    data.append({"title": title, "url": link, "image": image})
                    print(f"Added article: {title[:50]}...")

                    # Stop if we have 6 articles
                    if len(data) >= 6:
                        break
                except Exception as e:
                    print(f"Error processing article: {e}")
                    continue
        except Exception as e:
            print(f"Error finding global-leading-articles-big: {e}")

        print(f"Total articles scraped: {len(data)}")
        return data
