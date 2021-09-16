
import requests, bs4
page = requests.get('https://wiki.archlinux.org/index.php?search=py&title=Special%3ASearch&go=Go')
soup = bs4.BeautifulSoup(page.content, "html.parser")
titles = soup.find_all( class_ = "mw-search-result", limit=9)


for titlue in titles:
    print(titlue.get_text().split(' ')[0])
