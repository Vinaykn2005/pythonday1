class ShoppingCart:
    def __init__(self):
        self.item = {}
    def __getitem__(self,index):
        return self.item[index]
    def __setitem__(self, index, value):
        self.item[index] = value
cart = ShoppingCart()
cart[1] = "Shopping"
print(cart[1])