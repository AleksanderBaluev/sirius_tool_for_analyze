from bs4 import BeautifulSoup
import lxml
import requests

def remove_stop_words(text, stop_words):
    for word in stop_words:
        text = text.replace(word, "")
    return text

stop_words = ["Здравствуйте!","Здравствуйте.","Приветствуем.","Приветствуем!"]

url = "https://brobank.ru/banki/tinkoff/comments/"

headers  = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

src = req.text

    
soup  = BeautifulSoup(src, "lxml")

otzivi_tags = soup.find_all("article", class_="comment")


with open("otzivi.txt", "w", encoding="utf-8") as file:
    for item in otzivi_tags:
        special_el = item.find("p")
        otzivi = special_el.text
        clean_otzivi = remove_stop_words(otzivi, stop_words)
        file.write(clean_otzivi + "\n\n")
            
# comment-content comment

