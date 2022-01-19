
class Item:
    name = ""
    price = 0
    quantity = 0

    def __init__(self,name,price,quantity):
        self.name = name
        assert price >= 0, f"Il prezzo {price} è minore di 0"
        self.price = price
        assert quantity >= 0, f"La quantità {quantity} è minore di 0"
        self.quantity = quantity
        
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name

    def get_price(self):
        return self.price
    def set_price(self,price):
        assert price >= 0, f"Il prezzo {price} è minore di 0"
        self.price = price

    def get_quantity(self):
        return self.quantity
    def set_quantity(self,quantity):
        assert quantity >= 0, f"La quantità {quantity} è minore di 0"
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity



if __name__ == "__main__":

    item1 = Item("Phone", 100, 5)
    print("Prezzo Phone: ", item1.calculate_total_price())

    item2 = Item("Laptop", 1000, 3)
    print("Prezzo Laptop: ", item2.calculate_total_price())




