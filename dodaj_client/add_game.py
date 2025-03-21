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
    game_title2 = game_title.replace(" ", "")
    cleared_title = re.sub(r'[^A-Za-z0-9\s]', '', game_title2)
    with open(f'./{cleared_title}.jpg', "wb") as file:
        file.write(image_link.content)
    cover_path = f'./{cleared_title}.jpg'
    remote_control.send_cover_image(cover_path, f'{cleared_title}.jpg')
    os.remove(f'./{cleared_title}.jpg')
    remote_cover_path = f'static/cover/{cleared_title}.jpg'
    author = soup.find(class_="un-link").getText()
    item_type = "gra komputerowa"
    try:
        score = soup.find(class_="score").getText("score")
    except AttributeError:
        score = 0
    ean = "Brak"
    return game_title, author, description, link, ean, score, cover_path, item_type



