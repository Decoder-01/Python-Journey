class Item:

    def __init__(self, name: str, price: int, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):



Item1 = Item("laptop", 23, 4)


p





