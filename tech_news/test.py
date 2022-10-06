from scraper import fetch, scrape_noticia

url1 = 'https://blog.betrybe.com/carreira/passos-'
url2 = 'fundamentais-para-aprender-a-programar/'

url = url1 + url2


html = fetch(url)


scrape_noticia(html)

# scrape_next_page_link(html)


# scrape_novidades(html)
