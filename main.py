# How to create a class:
class Item:
    name = ""
    price = 0
    quantity = 0

    def __init__(self,name,price,quantity):
        self.name = name
        if price > 0:
            self.price = price
        else:
            print("Il prezzo deve essere > 0")
        if quantity > 0:
            self.quantity = quantity
        else:
            print("La qauntità deve essere > 0")

    def calculate_total_price(self):
        return self.price * self.quantity

# How to create an instance of a class
item1 = Item("Phone", 100, 5)

# Calling methods from instances of a class:
print(item1.calculate_total_price())


