class Product:
    def __init__(self, size, color):
        self.size=size
        self.color=color
    def sizes(self):
        return self.size
    def colors(self):
        return self.color

class Pant(Product):
    def __init__(self, size, color, material):
        super().__init__(size, color)
        self.material=material
    def materials(self):
        return self.material
class Tshirt(Product):
    def __init__(self, size, color, design):
        super().__init__(size, color)
        self.design=design
    def designs(self):
        return self.design

product=Pant(30,'Black','Jeans')
print(product.sizes())