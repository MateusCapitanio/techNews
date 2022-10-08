from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {'title': {'$regex': title, '$options': 'i'}}
    response = search_news(query)
    result = list()
    for new in response:
        result.append((new['title'], new['url']))
    return result


# Requisito 7
def search_by_date(date):
    try:
        date_converted = datetime.fromisoformat(date).strftime('%d/%m/%Y')
        query = {'timestamp': {'$regex': date_converted, '$options': 'i'}}
        response = search_news(query)
        result = list()
        for new in response:
            result.append((new['title'], new['url']))
        return result
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    query = {'tags': {'$elemMatch': {'$regex': tag, '$options': 'i'}}}
    response = search_news(query)
    result = list()
    for new in response:
        result.append((new['title'], new['url']))
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
