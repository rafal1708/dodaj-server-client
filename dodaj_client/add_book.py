import requests
from bs4 import BeautifulSoup
import remote_control
import os
import re

def add_book(args):
    link = args.link
    content = requests.get(link).text
    soup = BeautifulSoup(content, "html.parser")
    description = soup.find(id="book-description").getText()
    book_rate_raw = soup.find(class_="rating-value__img")["alt"]
    full_rate = (book_rate_raw[1:]).replace(",",".")
    full_rate = float(full_rate)
    raw_book_title = soup.find(class_="book__title").getText()
    book_title = raw_book_title.strip()
    title = book_title.replace(" ", "")
    cleared_title = re.sub(r'[^A-Za-z0-9\s]', '', title)
    ean_nr = soup.find(property="books:isbn")["content"]
    ean = f"EAN: {ean_nr}"
    image = soup.find(class_="overflow-hidden book-cover__link")["data-cover"]
    author = soup.find(property="books:author")["content"]
    image_link = requests.get(image)
    image_file = image_link.content
    book_type = soup.find(class_="book__category d-sm-block d-none").getText()
    if "komiksy" in book_type:
        book_type = "komiks"
    else:
        book_type = "książka"
    with open(f"./{cleared_title}.jpg", "wb") as file:
        file.write(image_file)
    cover_path = f"./{cleared_title}.jpg"
    remote_control.send_cover_image(cover_path, f"{cleared_title}.jpg")
    os.remove(f"./{cleared_title}.jpg")
    remote_cover_path = f'static/cover/{cleared_title}.jpg'
    return book_title, author, description, link, ean, full_rate, remote_cover_path, book_type





