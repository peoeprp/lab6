class Restaurant():
    restaurant_rating="5"
    def __init__(self, restaurant_name, cuisine_type,restaurant_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_rating=restaurant_rating

    def describe_restaurant(self):
        return "Название ресторана: %s, Тип кухни: %s " % (self.restaurant_name, self.cuisine_type)
    def open_restaurant(self):
        return "Ресторан открыт"
    def reit(self):
        rei=input("Введите рейтинг: ")
        if self.restaurant_rating != rei:
            self.restaurant_rating=rei
            return "Новый рейтинг: %s" % (int(self.restaurant_rating))


newRestaurant = Restaurant(input("Введите название ресторана: "),input("Введите тип кухни: "), "5")
print("Название ресторана: ", newRestaurant.restaurant_name)
print("Тип кухни: ", newRestaurant.cuisine_type)
print("Рейтинг ресторана: ", newRestaurant.restaurant_rating)
print(newRestaurant.describe_restaurant())
print(newRestaurant.open_restaurant())
print(newRestaurant.reit())
