from scraper import fetch, scrape_novidades, scrape_next_page_link


url = "https://blog.betrybe.com/"


html = fetch(url)

scrape_next_page_link(html)


# scrape_novidades(html)
