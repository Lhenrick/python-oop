from models.restaurant import Restaurant

restaurant_omise = Restaurant('omise', 'Japanese')
restaurant_lechefe = Restaurant('le Chef', 'French')
restaurant_tortilha = Restaurant('tortilhas', 'mexican')
restaurant_tortilha.receive_review('luan', 9)
restaurant_tortilha.receive_review('Ana', 7)
restaurant_tortilha.receive_review('Paula', 7)



restaurant_tortilha.change_state()

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()