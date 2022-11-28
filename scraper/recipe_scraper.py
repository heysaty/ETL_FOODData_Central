from bs4 import BeautifulSoup
import requests

def scraper(fooditem):
    url = 'https://recipes.timesofindia.com/searchresults.cms?query=' + fooditem

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find_all('span', attrs={'class': 'posrel'})

    recipe_url = str(content[0]).split('"')

    recipe_page = requests.get(recipe_url[3])

    recipe_soup = BeautifulSoup(recipe_page.content, 'html.parser')

    recipe_content = recipe_soup.find_all('p')
    recipe = ''

    for line in recipe_content[-7:-1]:
        try:
            line = str(line).replace('<p>', '')
            line = line.replace('</p>', '')
            recipe += line

        except:
            pass
    recipe = recipe.replace("'", '')
    recipe = recipe.replace("<br/>", '')
    return recipe
