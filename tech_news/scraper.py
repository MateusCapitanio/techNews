import requests
import time

url = "https://blog.betrybe.com/"


def fetch(url, timeout=3):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent", "Accept": "text/html"},
            timeout=timeout
        )
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    finally:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
