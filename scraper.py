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
    foods = soup.find_all('li', class_='filter_target')
    for food in foods:
        category_element = food.find_previous('h2')
        food_category = category_element.get_text(strip=True)
        if food:
            restaurant_foods.append({
                'food_name': food['title'],
                'food_calories': food['data-calories'],
                'food_restaurant': restaurant,
                'food_logo': "https://fastfoodnutrition.org" + restaurant_logo,
                'food_category': food_category,
                'food_link': "https://fastfoodnutrition.org" + food.find('a').get('href')
            })

    return restaurant_foods

def scrape_picture(html):
    ...
