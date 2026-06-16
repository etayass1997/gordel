import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
}

def scrape_url(url, timeout=15):
    resp = requests.get(url, headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside', 'form']):
        tag.decompose()

    title = soup.title.string.strip() if soup.title else url

    # Try main content areas first
    main = (soup.find('article') or soup.find('main') or
            soup.find(id=re.compile(r'content|main|article', re.I)) or
            soup.find(class_=re.compile(r'content|main|article|post', re.I)) or
            soup.body)

    if not main:
        return '', title

    text = main.get_text(separator='\n')
    # Normalize whitespace
    lines = [l.strip() for l in text.splitlines()]
    text = '\n'.join(l for l in lines if l)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text[:15000], title
