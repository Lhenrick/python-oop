from models.review import Review
from models.menu.menu_item import MenuItem


class Restaurant:
    restaurants = []

    def __init__(self, _name, _category):
        self._name = _name.title()
        self._category = _category.upper()
        self._active = False
        self._score = []
        self._menu = []
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f'{self._name} | {self._category}'
    
    @classmethod
    def list_restaurants(cls):
        print(f'{'Restaurant Name'.ljust(25)} | {'Category'.ljust(25)} | {'Review'.ljust(25)} | {'status'}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_score).ljust(25)} | {restaurant.active}')
        
    @property
    def active(self):
        return '✅' if self._active else '❌'

    def change_state(self):
        self._active = not self._active

    
    def receive_review(self, customer, score):
        if  0 < score <=5: 
            review = Review(customer, score)
            self._score.append(review)
        

    @property
    def average_score(self):
        if not self._score:
            return ''
        score_sum = sum(review._score for review in self._score)
        score_number = len(self._score)
        average = round(score_sum / score_number, 1)
        return average

    def add_to_menu(self, item):
        if isinstance(item, MenuItem):
            self._menu.append(item)
    @property
    def display_menu(self):
        print(f"{self._name}'s menu\n")
        for i,item in enumerate(self._menu, start=1):
            if hasattr(item, 'description'):
                message_meal = f'{i}. Name: {item._name} | Price: R$ {item._price} | Description: {item.description}'
                print(message_meal)
            else:
                message_drink = f'{i}. Name: {item._name} | Price: R$ {item._price} | Size: {item.size}'
                print(message_drink)