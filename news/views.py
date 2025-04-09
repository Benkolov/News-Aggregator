import requests
from concurrent.futures import ThreadPoolExecutor
from django.shortcuts import render, redirect
from news.models import Headline
from news.scrapers.bbc_scraper import BBCScraper
from news.scrapers.webcafe_scraper import WebcafeScraper
from news.scrapers.dnevnik_scraper import DnevnikScraper
from news.scrapers.gong_scraper import GongScraper

def scrape_multiple_sites(request):
    headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    session = requests.Session()
    session.headers.update(headers)

    scrapers = [
        BBCScraper("https://www.bbc.com/news", "BBC"),
        DnevnikScraper("https://www.dnevnik.bg/novini/dnes/", "Dnevnik"),
        WebcafeScraper("https://webcafe.bg/newscafe", "Webcafe"),
        GongScraper("https://gong.bg/", "Gong"),
    ]

    data = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(scraper.parse) for scraper in scrapers]
        for future in futures:
            try:
                data.extend(future.result())
            except Exception as e:
                print(f"Грешка при парсване: {e}")

    for scraper in scrapers:
        scraper.close()

    return redirect("home")


def scrape_single_source(request, source):
    headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    session = requests.Session()
    session.headers.update(headers)

    scraper_map = {
        'dnevnik': DnevnikScraper("https://www.dnevnik.bg/novini/dnes/", "Dnevnik"),
        'webcafe': WebcafeScraper("https://webcafe.bg/newscafe", "Webcafe"),
        'bbc': BBCScraper("https://www.bbc.com/news", "BBC"),
        'gong': GongScraper("https://gong.bg/", "Gong"),
    }

    if source in scraper_map:
        scraper = scraper_map[source]
        try:
            scraper.parse()
        except Exception as e:
            print(f"Грешка при парсване на {source}: {e}")
        finally:
            scraper.close()

    return redirect("home")


def news_list(request):
    all_sources = ["Dnevnik", "Webcafe", "BBC", "Gong"]
    headlines = Headline.objects.all().order_by('-id')

    news_by_source = {}
    for source in all_sources:
        news_by_source[source] = headlines.filter(source=source)[:6]
    
    return render(request, "news/home.html", {
        'news_by_source': news_by_source,
        'sources': all_sources
    })
