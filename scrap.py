from bs4 import BeautifulSoup # type: ignore
import requests # type: ignore

# website = "https://subslikescript.com/movie/Titanic-120338"

# def beautiful_soup_view(request):
#     result = requests.get(website)
#     content = result.text
#     soup = BeautifulSoup(content, 'lxml')
#     # print(soup.prettify())

#     box = soup.find('article', class_='main-article')
#     title = box.find('h1').get_text()
#     transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
#     with open(f'{title}.txt', 'w') as file:
#         file.write(transcript)

#     return render(request, 'core/test.html')
root = 'https://subslikescript.com/'
website = f"{root}movies"

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')
links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

print(links)
for link in links:
    websitelink = f"{root}{link}"
    result = requests.get(websitelink)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
    with open(f'files/{title}.txt', 'w', encoding='utf-8') as file:
        file.write(transcript)

