import requests
import time
from parsel import Selector

url = "https://blog.betrybe.com/"


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    responseTags = selector.css(
        '.archive-main .entry-preview .entry-title a::attr(href)'
    ).getall()
    return responseTags


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    responseTags = selector.css(
        '.cs-container .post-archive .navigation .nav-links .next::attr(href)'
    ).get()
    return responseTags


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css('head link[rel=canonical]::attr(href)').get()
    title = selector.css(
        '.entry-header-inner .entry-title::text'
    ).get().rstrip()
    timestamp = selector.css('.meta-date::text').get()
    author = selector.css('li.meta-author .author a::text').get()
    comments_count = selector.css(
        'div.post-comments h5.title-block::text'
    ).get()
    if comments_count is None:
        comments_count = 0
    text = selector.xpath("string(//p)").get().rstrip()
    tags = selector.css(
        'div.entry-content-wrap .post-tags ul li a::text'
    ).getall()
    if tags is None:
        tags = []
    category = selector.css('div.meta-category a span.label::text').get()

    data = ({
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": author,
        "comments_count": comments_count,
        "summary": text,
        "tags": tags,
        "category": category,
    })
    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
