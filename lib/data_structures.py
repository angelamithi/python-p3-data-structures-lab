spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    foods_with_spice=[food["name"] for food in spicy_foods]
    return foods_with_spice
foods=get_names(spicy_foods)
print(foods)

def get_spiciest_foods(spicy_foods):
    spiciest_foods=[food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods
spiciest_foods=get_spiciest_foods(spicy_foods)
print(spiciest_foods)
   

def print_spicy_foods(spicy_foods):
    [print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}") for food in spicy_foods]
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_foods_by_cuisine=[food for food in spicy_foods if food['cuisine']==cuisine]
    return spicy_foods_by_cuisine
cuisine_food=get_spicy_food_by_cuisine(spicy_foods,"American")
print(cuisine_food)
    

def print_spiciest_foods(spicy_foods):
    [print(f"{food['name']} ({food['cuisine']}) | Heat Level:{'🌶' * food['heat_level']}") for food in spicy_foods if food['heat_level'] > 5]
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level=sum(food["heat_level"]for food in spicy_foods)
    average_heat_level=total_heat_level/ len(foods) 
    return int(average_heat_level)
spicy_food_average_heat_level=get_average_heat_level(spicy_foods)
print(spicy_food_average_heat_level)

def create_spicy_food(spicy_foods, spicy_food):
    add_spicy_food=spicy_foods.copy()
    add_spicy_food.append(spicy_food)

    return add_spicy_food

updated_spicy_food=create_spicy_food(spicy_foods,{ "name":"curry","cuisine":"Kenyan","heat_level":8})
print(updated_spicy_food)