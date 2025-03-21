import requests
from bs4 import BeautifulSoup
#import remote_control
import os
import urllib.parse


def add_movie(args):
    link = args.link
    content = requests.get(link)
    soup = BeautifulSoup(content.text, "html.parser")
    with open("./nwe.html", "w") as f:
        f.write(soup.prettify())
    
    data = soup.find("meta", property="og:title")["content"].split("|")
    remote_cover_path = soup.find("img", {"id":"filmPoster"})["src"]
    
    try:
        movie_title = data[0].strip()
        movie_type = data[1].strip()
        year = data[2].strip()
    except IndexError:
        link_parts = link.split("/")
        title_and_year = link_parts[4]
        raw_movie_title = title_and_year.split("-")[0] 
        year = title_and_year.split("-")[1] #Zapisane na zaś, na razie nie jest używane
        movie_title = urllib.parse.unquote(raw_movie_title.replace("+"," "))
        movie_type = link_parts[3]
    desc = soup.find_all(itemprop="description")
    description = desc[0].get_text()
    raw_tags = soup.find_all("span",{"itemprop":"genre"})
    tags_list = []
    for i in raw_tags:
        genre = i.text.strip()
        tags_list.append(genre)
        ean = ", ".join(tags_list) # iteruje po tagach filmu, tworzy listę a potem iteruje po liście, tworząc string. To nie żaden EAN :D Nazwę zostawiłem by pasowała do nazw przekazywanych wartości do bazy danych ale warto to poukładać bardziej logicznie
    author = ""
    director = soup.find("a", itemprop="director")
    creator = soup.find("a", itemprop="creator")

    if director and "title" in director.attrs:
        author = director["title"]
    elif creator:
        author = creator.get_text(strip=True)
    else:
        author = "Być może wielu autorów"
    try:
        raw_rate = soup.find("span", itemprop="ratingValue").getText().strip()
        full_rate = float(raw_rate.replace(",","."))
    except:
        full_rate = 0

    return movie_title, author, description, link, ean, full_rate, remote_cover_path, movie_type

