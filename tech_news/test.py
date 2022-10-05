from scraper import fetch, scrape_novidades


url = "https://blog.betrybe.com/"


html = fetch(url)


scrape_novidades(html)
