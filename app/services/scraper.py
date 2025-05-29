import requests
from bs4 import BeautifulSoup

def get_html_from_url(url: str) -> str:

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    return str(soup)
