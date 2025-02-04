from django.urls import path
from news.views import scrape_multiple_sites, news_list
urlpatterns = [
  path('scrape/', scrape_multiple_sites, name="scrape"),
  path('', news_list, name="home"),
]