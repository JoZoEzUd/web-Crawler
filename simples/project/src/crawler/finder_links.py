from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extrair_links(base_url, html):
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for tag in soup.find_all("a"):
        href = tag.get("href")
        if not href:
            continue
        final= urljoin(base_url, href)
        links.append(final)

    return list(set(links))