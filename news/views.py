import requests
from concurrent.futures import ThreadPoolExecutor
from django.shortcuts import render, redirect
from news.models import Headline
from news.scrapers.bbc_scraper import BBCScraper
from news.scrapers.webcafe_scraper import WebcafeScraper
from news.scrapers.dnevnik_scraper import DnevnikScraper


def scrape_multiple_sites(request):
    headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    session = requests.Session()
    session.headers.update(headers)

    scrapers = [
        DnevnikScraper("https://www.dnevnik.bg"),
        WebcafeScraper("https://webcafe.bg/newscafe"),
        BBCScraper("https://www.bbc.com/news"),
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

def news_list(request):
    headlines = Headline.objects.all().order_by('-id')
    return render(request, "news/home.html", {'object_list': headlines})
