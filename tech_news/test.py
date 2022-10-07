from scraper import (
    fetch,
    # scrape_noticia
    # scrape_novidades
    get_tech_news,
    # scrape_next_page_link
)

url = 'https://blog.betrybe.com/'


html = fetch(url)


# scrape_noticia(html)
get_tech_news(2)

# scrape_next_page_link(html)


# scrape_novidades(html)
