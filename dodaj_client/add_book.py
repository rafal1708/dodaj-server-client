import requests
from bs4 import BeautifulSoup
import remote_control
import os

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
    cleared_title = book_title.replace(" ", "")
    ean = soup.find(property="books:isbn")["content"]
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
    remote_cover_path = f'static/book_cover/{cleared_title}.jpg'
    return book_title, author, description, link, ean, full_rate, remote_cover_path, book_type






