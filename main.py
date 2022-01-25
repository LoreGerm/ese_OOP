import csv


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
        if self.is_integer(quantity):
            self.quantity = quantity
        self.all_items.append(self)

    def get_all_items(self):
        return self.all_items

    def calculate_total_price(self):
        return self.price * self.quantity

    def calculate_discout(self,discount=pay_rate):
        return discount * self.price

    def __repr__(self):
        return f"item({self.name}, {self.price}, {self.quantity})"

    @staticmethod
    def is_integer(num):
        try:
            int(num)
            return True
        except:
            return False

    @staticmethod
    def read_from_csv():
        f = csv.DictReader(open('item.csv'))
        a = []
        for row in f:
            if Item.is_integer(row['quantity']) == True:
                a.append(row)
        return a




if __name__ == "__main__":

    item1 = Item("Phone", 100, 5)
    print("Prezzo Phone: ", item1.calculate_total_price())

    item2 = Item("Laptop", 1000, 3.90)
    print("Prezzo Laptop: ", item2.calculate_total_price())
    print(item1.get_all_items())

    print("Sconto Item1" ,item1.calculate_discout())
    print(item1,", ", item2)

    print(Item.read_from_csv())




