# dodaj
Tworzenie lokalnej bazy książek i gier w oparciu o webscarping strony lubimyczytac i gry-online.

Wymaga zewnętrznych bibliotek - bs4 i flask

Program "dodaj", dodaje pozycję z linka do bazy danych.
sqlread.py odczytuje tę bazę i wyświetla w przeglądarce pod adresem:</br>
IP-komputera:5050/[książki|komiksy|gry]

<h2>Sposób użycia:</h2>

Dodanie strony do bazy danych: dodaj link-do-strony</br>
Usunięcie strony z bazy danych: dodaj -d link-do-strony</br>
Dodanie strony z własnym komentarzem lub zmiana/dodanie komentarza do istniejącej już w bazie pozycji: dodaj -n link-do-strony</br>

<h3>API</h3>
IP-komputera:5050/api</br>
Możliwość wyszukiwania wg parametrów:</br>  
"category" - "ksiazka", "komiks", "gra komputerowa"</br>
"tag" - dowolne słowo. Przeszukiwany będzie opis danej pozycji i pole z własnym komentarzem</br>
"author" - wyszukuje w kolumnie "author" pasującego słowa </br>
"rate" - czyli wg minimalnej oceny danej pozycji podanej na stronie.</br>

Testowane na Linuxie, rhel 8

