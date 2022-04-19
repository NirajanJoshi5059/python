class Pant:
    def __init__(self, price, size):
        self.prices=price
        self.sizes=size
    def price(self):
        print(f"Price of pant is {self.prices} ")
    def size(self):
        print(f"Size of pantis {self.sizes}")
pant1=Pant(1500,32)
pant1.size()
pant1.price()
