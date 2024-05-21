import requests
from bs4 import BeautifulSoup


def parseHTML(request_url):
    login_basic_url = 'https://mbasic.facebook.com/login'
    payload = {
        'email': "7981176194",
        'pass': "sonu2001"
    }
    with requests.Session() as session:
        post = session.post(login_basic_url, data=payload)
        parsed_html = session.get(request_url)
    return parsed_html


def get_cars():
    text = parseHTML("https://www.facebook.com/marketplace/manila/cars?minPrice=350000&exact=false")
    d = {}
    html_text = requests.get("https://www.facebook.com/marketplace/manila/cars?minPrice=350000&exact=false").text
    soup = BeautifulSoup(html_text, 'lxml')
    soup.prettify()


if __name__ == '__main__':
    get_cars()
