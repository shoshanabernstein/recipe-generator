import sqlite3
from scraper import scrape_restaurant

def create_database():
    """Creates the database"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS restaurant_foods (
                id INTEGER PRIMARY KEY,
                food_name TEXT,
                food_calories INT,
                food_restaurant TEXT,
                food_logo BLOB,
                food_category TEXT,
                food_link TEXT
            )
        ''')
    conn.commit()

def load_databse(foods):
    """Loads the data into the databse"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        
        for food in foods:
            c.execute('''
                INSERT INTO restaurant_foods(food_name, food_calories, food_restaurant, food_logo, 
                      food_category, food_link) VALUES (?, ?, ?, ?, ?, ?)
            ''', (food['food_name'], food['food_calories'], food['food_restaurant'], 
                  food['food_logo'], food['food_category'], food['food_link']))

    conn.commit()

def filter_foods(restaurant=None, calories=None, category=None): 
    """Filters the foods by restaurant, calories, and category and returns a list of foods"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()

        query = f"""SELECT food_name, food_calories, food_restaurant, food_logo, food_category, food_link
        FROM restaurant_foods
        WHERE 1=1
        """
        params = []

        if restaurant:
            query += " AND food_restaurant = ?"
            params.append(restaurant)
        
        if calories:
            query += " AND food_calories <= ?"
            params.append(calories)

        if category:
             query += " AND food_category = ?"
             params.append(category)
             
        c.execute(query, tuple(params))

        rows = c.fetchall() 
        filter_foods = []

        for row in rows:
                food_name, food_calories, food_restaurant, food_logo, food_category, food_link = row

                filter_foods.append({
                        "food_name": food_name,
                        "food_calories": food_calories,
                        "food_restaurant": food_restaurant,
                        "food_logo": food_logo,
                        "food_category": food_category,
                        "food_link": food_link
                    })

    return filter_foods

def get_food_categories():
    """Get list of food categories"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT food_category FROM restaurant_foods GROUP BY food_category''')

        rows = c.fetchall()

    categories = []
    for row in rows:
        categories.append(row[0])
    return categories

def get_food_restaurant():
    """Get list of food restaurant"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT food_restaurant FROM restaurant_foods GROUP BY food_restaurant''')

        rows = c.fetchall()

    restaurant = []
    for row in rows:
        restaurant.append(row[0])
    return restaurant

def get_categories_by_restaurant(restaurant):
    """Get list of categpries by food restaurant"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT DISTINCT food_category 
                FROM restaurant_foods 
                WHERE food_restaurant = ?''', (restaurant,))

        rows = c.fetchall()

    restaurant = []
    for row in rows:
        restaurant.append(row[0])
    return restaurant


if __name__=="__main__":
    create_database()

    mcdonalds = scrape_restaurant("https://fastfoodnutrition.org/mcdonalds")
    wendys = scrape_restaurant("https://fastfoodnutrition.org/wendys")
    starbucks = scrape_restaurant("https://fastfoodnutrition.org/starbucks")
    dairy_queen = scrape_restaurant("https://fastfoodnutrition.org/dairy-queen")
    load_databse(mcdonalds)
    load_databse(wendys)
    load_databse(starbucks)
    load_databse(dairy_queen)