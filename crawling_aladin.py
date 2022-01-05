"""
Thanks to the Third Party Libs
    https://github.com/zzsza/github-action-with-python
"""
import requests
from bs4 import BeautifulSoup


def parsing_beautifulsoup(url):
    """
    뷰티풀 수프로 파싱하는 함수
    :param url: paring할 URL. 여기선 알라딘 Link
    :return: BeautifulSoup soup Object
    """

    data = requests.get(url)

    html = data.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def extract_book_data(soup):
    """
    BeautifulSoup Object에서 book data를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """

    upload_contents = ''
    new_books = soup.select(".ss_book_box")

    for new_book in new_books:
        book_name = new_book.select(".bo3")[0].text
        url = new_book.select(".bo3")[0].attrs['href']
        price = new_book.select(".ss_p2")[0].text
        
        content = f"[{book_name}]({url})" + ", " + price + "<br/>\n"
        upload_contents += content

    return upload_contents