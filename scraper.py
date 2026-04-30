import requests
from bs4 import BeautifulSoup
import re

def scrape_restaurant(html):
    """Scrapes the menu from the provided URL and returns the scraped data"""
    r = requests.get(f'{html}', auth=('user', 'pass'))
    soup = BeautifulSoup(r.text, 'html.parser')  
    restaurant_foods = []

    # Scrape the restaurant name and logo
    restaurant = soup.find('div', class_='rest_links_name').text.strip()
    restaurant_logo = soup.find('img', class_='logo_float').get('src')
    
    # Scrape the menu items, their categories, and their calorie information
    categories = soup.find_all('a', class_='toggle_category topround nomobileround toggle_div')

    for category in categories:
        category = re.split(r"\d+", category.text)[0].strip()
        foods = soup.find_all('li', class_='filter_target')

    # Loop through the foods and extract the relevant information
        for food in foods:
            if food:
                restaurant_foods.append({
                    'food_name': food['title'],
                    'food_calories': food['data-calories'],
                    'food_restaurant': restaurant,
                    'food_logo': "https://fastfoodnutrition.org" + restaurant_logo,
                    'food_category': category,
                    'food_link': "https://fastfoodnutrition.org" + food.find('a').get('href')
                })

    return restaurant_foods
 