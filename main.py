import csv


class Item:  #My first class
    all_items = []
    item_discount = 0.5

    def __init__(self, name: str, price: int, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity
    def add_discount(self):
        return self.price * self.item_discount
    @classmethod
    def initiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            iterator = csv.DictReader(f)
            items = list(iterator)
        for item in items:
            print(item)
            Item1.all_items.append(item)

    def calculate_total_price(self):
        return self.price * self.quantity
    def __repr__(self):
        return f"item({self.name},{self.price},{self.quantity})"


Item1 = Item("laptop", 500, 1)

print("The Total price for the first item is:",Item1.calculate_total_price(),"naira",sep=" ")
print("the price after adding discount is",Item1.add_discount())
print(Item1.initiate_from_csv())




