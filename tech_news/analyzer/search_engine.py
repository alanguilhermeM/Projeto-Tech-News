import re
from tech_news.database import db
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
        result = list(db.news.find({'timestamp': regex_query}))

        return [(entry['title'], entry['url']) for entry in result]
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
