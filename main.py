class Item:  #My first class
    all_items = []
    item_discount = 0.5

    def __init__(self, name: str, price: int, quantity=0): #I created a method to take three parameters for a which is name price and quantity
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"  #this function of this assert keyword is to give an error message if the price parameter is less than 0"""
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"  #Likewise this also for the quantity because it shouldn't be less than zero"""

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_items.append(self)
    def add_discount(self):
        return self.price * self.item_discount

    def calculate_total_price(self):

        return self.price * self.quantity
    def __repr__(self):
        return f"item('{self.name}','{self.price}','{self.quantity}')"


Item1 = Item("laptop", 500, 1)

print("The Total price for the first item is:",Item1.calculate_total_price(),"naira",sep=" ")
print("the price after adding discount is",Item1.add_discount())
print(Item1.all_items)




