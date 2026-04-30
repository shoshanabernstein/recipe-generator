import requests
from bs4 import BeautifulSoup
import re

def scrape_starbucks(html):
    r = requests.get(f'{html}', auth=('user', 'pass'))
    soup = BeautifulSoup(r.text, 'html.parser')  
    soup2 = BeautifulSoup()

    restaurant = soup.find('h2', class_='mobile_padding').text.strip
    
    print(restaurant)
    categories = soup.find_all('a', class_='toggle_category topround nomobileround toggle_div')
    for category in categories:
        category = re.split(r"\d+", category.text)[0].strip()
        foods = soup.find_all('li', class_='filter_target')
        for food in foods:
            if food:
                food_link =link = soup.find('a', attrs={"href"})
                food_calories = food['data-calories']
                food_name = food['title']
                food_category = category
            print(food_name)
            # print(food_category)
            # print(food_calories)
            print(food_link)

   
scrape_starbucks("https://fastfoodnutrition.org/mcdonalds")