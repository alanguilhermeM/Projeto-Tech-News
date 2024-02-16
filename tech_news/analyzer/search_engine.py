import re
from ..database import db


# Requisito 7
def search_by_title(title):
    regex_query = re.compile(f'.*{title}.*', re.IGNORECASE)
    result = list(db.news.find({'title': regex_query}))

    return [(entry['title'], entry['url']) for entry in result]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
