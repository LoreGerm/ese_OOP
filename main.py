
class Item:
    name = ""
    price = 0
    quantity = 0
    pay_rate = 0.8
    all_items = []

    def __init__(self,name,price,quantity):
        self.name = name
        assert price >= 0, f"Il prezzo {price} è minore di 0"
        self.price = price
        assert quantity >= 0, f"La quantità {quantity} è minore di 0"
        self.quantity = quantity
        #item = [self.get_name(),self.get_price(),self.get_quantity()]
        self.all_items.append(self)
        
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

    def get_pay_rate(self):
        return self.pay_rate
    def set_pay_rate(self,pay_rate):
        self.pay_rate = pay_rate

    def get_all_items(self):
        return self.all_items

    def calculate_total_price(self):
        return self.price * self.quantity

    def calculate_discout(self,discount=pay_rate):
        return discount * self.price

    def __repr__(self):
        return f"item({self.name}, {self.price}, {self.quantity})"



if __name__ == "__main__":

    item1 = Item("Phone", 100, 5)
    print("Prezzo Phone: ", item1.calculate_total_price())

    item2 = Item("Laptop", 1000, 3)
    print("Prezzo Laptop: ", item2.calculate_total_price())
    print(item1.get_all_items())

    print("Sconto Item1" ,item1.calculate_discout())
    print(item1,", ", item2)





