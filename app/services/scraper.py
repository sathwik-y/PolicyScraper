import requests
from bs4 import BeautifulSoup

def get_html_from_url(url: str) -> str:
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'Accept-Language': 'en-US,en;q=0.5',
    #     'Accept-Encoding': 'gzip, deflate',
    #     'Connection': 'keep-alive',
    #     'Upgrade-Insecure-Requests': '1',
    # }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    return str(soup) 

# from requests_html import HTMLSession

# def get_html_from_url(url: str) -> str:
#     session = HTMLSession()
#     try:
#         r = session.get(url)
#         r.html.render(timeout=20)  
#     except Exception as e:
#         r = session.get(url)
#         return r.html.html