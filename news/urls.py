from django.urls import path
from news.views import scrape_multiple_sites, news_list, scrape_single_source

urlpatterns = [
    path('scrape/', scrape_multiple_sites, name="scrape"),
    path('scrape/<str:source>/', scrape_single_source, name="scrape_source"),
    path('', news_list, name="home"),
]