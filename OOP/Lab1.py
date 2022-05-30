# LAB 1 - OOP
# Create one class called FruitShop. This class should receive a name which should be a string, and fruits as a list.
# Create also a method called get_fruits_count() which should return amount of fruits in the shop.
# Input:
# my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi", "Apple"])
# Output: 4


class FruitShop:
    def __init__(self, name, fruits_list):
        self.name = name
        self.fruits_list = fruits_list

    def get_fruits_count(self):
        print(len(self.fruits_list))
            

my_shop = FruitShop("My Fruit Shop", ["Banana" , "Orange", "Kiwi", "Apple"])
my_shop.get_fruits_count()

