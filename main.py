class Item: #My first class

    def __init__(self, name: str, price: int, quantity=0): # I created a method to take three parameters for a which is name price and quantity
        assert price >= 0, f"Price {price} is not greater than or equal to zero!" #this function of this assert keyword is to give an error message if the price parameter is less than 0
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!" # Likewise this also for the quantity cause it shouldn't be less than zero

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):



Item1 = Item("laptop", 23, 4)


p





