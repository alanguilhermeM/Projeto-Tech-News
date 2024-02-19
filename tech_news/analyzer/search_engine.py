import re
from tech_news.database import db, search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    regex_query = re.compile(f'.*{title}.*', re.IGNORECASE)
    result = list(db.news.find({'title': regex_query}))

    return [(entry['title'], entry['url']) for entry in result]


# Requisito 8
def search_by_date(date):
    try:
        iso_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        regex_query = re.compile(f'.*{iso_date}.*', re.IGNORECASE)
        result = search_news({"timestamp": regex_query})

        return [(entry['title'], entry['url']) for entry in result]
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    regex_query = re.compile(f'.*{category}.*', re.IGNORECASE)
    result = search_news({"category": regex_query})
    if len(result) == 0:
        return []
    return [(entry['title'], entry['url']) for entry in result]
