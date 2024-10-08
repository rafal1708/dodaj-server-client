import mysql.connector
import configparser

def link_validation(link):
    try:
        if link.startswith("https://lubimyczytac.pl/ksiazka/") or link.startswith("https://www.gry-online.pl/gry/"):
            return True
        else:
            return False
    except AttributeError:
        return False


def is_item_in_database(link):
    config = configparser.ConfigParser()
    config.read("config_client.ini")
    db_dbname = config['wishlist_conf']['db_name']
    remote_sql_username = config['wishlist_conf']['remote_sql_username']
    remote_sql_password = config['wishlist_conf']['remote_sql_password']
    ip_server = config['wishlist_conf']['ip_server']
    db = mysql.connector.connect(host=ip_server, port=3306, user=remote_sql_username, password=remote_sql_password, database=db_dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * from my_wishlist WHERE link = %s", (link,))
    book = cursor.fetchall()
    db.close()
    if book:
        return True
    else:
        return False

def select_category(link):
    if link.startswith("https://lubimyczytac.pl/ksiazka/"):
        return "books"
    else:
        return "games"
