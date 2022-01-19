
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



if __name__ == "__main__":

    item1 = Item("Phone", 100, 5)
    total_price_1 = item1.calculate_total_price()
    print("Prezzo Phone: ", total_price_1)


    item2 = Item("Laptop", 1000, 3)
    total_price_2 = item2.calculate_total_price()
    print("Prezzo Laptop: ", total_price_2)




