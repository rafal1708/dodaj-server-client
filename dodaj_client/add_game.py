from bs4 import BeautifulSoup
import requests


def add_game(args):
    link = args.link
    content = requests.get(link).text
    soup = BeautifulSoup(content, "html.parser")
    description = soup.find(id="game-description-cnt").getText()
    #description = soup.find('p', itemprop='description').string - Lead of article
    image = soup.find(id="game-cover-src")["src"]
    image_link = requests.get(image)
    raw_game_title = soup.find(id="game-title-cnt").getText()
    game_title = raw_game_title.strip()
    cleared_game_title = game_title.replace(" ", "")
    with open(f"./static/cover/{cleared_game_title}.jpg", "wb") as file:
        file.write(image_link.content)
    cover_path = f"static/cover/{cleared_game_title}.jpg"
    author = soup.find(class_="un-link").getText()
    item_type = "gra komputerowa"
    try:
        score = soup.find(class_="score").getText("score")
    except AttributeError:
        score = 0
    ean = "Brak"
    return game_title, author, description, link, ean, score, cover_path, item_type



