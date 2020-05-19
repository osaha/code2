from lxml import etree
from io import StringIO
import requests, json
import xml.etree.ElementTree as et

def main(isbn):
    url_ndl =  'https://iss.ndl.go.jp/api/opensearch?isbn='
    url_google = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

    url_google += isbn
    response = requests.get(url_google)
    d = json.loads(response.text)
    title = d['items'][0]['volumeInfo']['title']
    authors = d['items'][0]['volumeInfo']['authors']
    publisheddate = d['items'][0]['volumeInfo']['publishedDate']

    url_ndl += isbn
    response = requests.get(url_ndl, headers = {'content-type': 'text/xml'})
    root = et.fromstring(response.content)
    title_ndl = root[0][7][0].text
    authors_ndl = root[0][7][9].text
    publisher_ndl = root[0][7][13].text
    publisheddate_ndl = root[0][7][6].text

    print(title, authors, publisheddate, '\n', title_ndl, authors_ndl,publisher_ndl,publisheddate_ndl, >
    return title, authors, publisheddate, title_ndl, authors_ndl,publisher_ndl,publisheddate_ndl



if __name__ == "__main__":
    while True:
        isbn_input = input("input ISBN >>>")
        main(isbn_input)
