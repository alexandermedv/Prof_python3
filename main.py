import requests
from bs4 import BeautifulSoup
from pprint import pprint


if __name__ == '__main__':
    key_words = ['PostgreSQL', 'Java', 'фронтенд', 'компиляция', 'Python', 'Программирование', 'Linux', 'GPT-3', 'C++']

    ret = requests.get('https://habr.com/ru/top/daily/')

    soup = BeautifulSoup(ret.text, 'html.parser')
    articles = soup.find_all('article')

    art_list = []
    for article in articles:
        art_dict = {}
        dt = article.find('span', class_='tm-article-snippet__datetime-published').find('time')
        title = article.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2')
        link = 'https://habr.com/ru/post/' + str(article["id"]) + '/'
        text = article.select('div[class*="article-formatted-body"]')[0].find('p')
        key = False
        for word in key_words:
            if text and word in text.text:
                key = True
        if key:
            art_dict['date'] = dt["title"][0:10]
            art_dict['title'] = title.text
            art_dict['link'] = link
            art_list.append(art_dict)
    pprint(art_list)
