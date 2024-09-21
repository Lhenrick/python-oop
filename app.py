from models.restaurant import Restaurant
from models.menu.drinks import Drink
from models.menu.meals import Meal


# restaurant_lechefe = Restaurant('le Chef', 'French')
# restaurant_tortilha = Restaurant('tortilhas', 'mexican')

restaurant_omise = Restaurant('omise', 'Japanese')
drink_juice = Drink('Orange Juice', 5.0, 'Large')
drink_juice.apply_discount()
meal_pasta = Meal('Pasta', 5.00, 'The finnest quality pasta')
meal_pasta.apply_discount()
restaurant_omise.add_to_menu(drink_juice)
restaurant_omise.add_to_menu(meal_pasta)


def main():
    restaurant_omise.display_menu

if __name__ == '__main__':
    main()