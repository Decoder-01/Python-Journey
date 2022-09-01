class Item: #My first class
    item_discount = 0.5

    def __init__(self, name: str, price: int, quantity=0): #I created a method to take three parameters for a which is name price and quantity
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"  #this function of this assert keyword is to give an error message if the price parameter is less than 0"""
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"  #Likewise this also for the quantity cause it shouldn't be less than zero"""

        self.name = name
        self.price = price
        self.quantity = quantity
    def add_discount(self):

        return self.price * self.item_discount

    def calculate_total_price(self):

        return self.price * self.quantity



Item1 = Item("laptop", 23, 4)





