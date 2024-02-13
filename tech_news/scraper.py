import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    # headers = {"user-agent": "Fake user-agent"}
    # response = requests.get(html_content, headers=headers)
    selector = Selector(text=html_content)
    news = []
    news = selector.css(".entry-thumbnail div a::attr(href)").getall()
    # print(news)
    if len(news) == 0:
        return []
    return news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".next.page-numbers::attr(href)").get()
    if next_page_link:
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
