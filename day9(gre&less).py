class Mobile:
    def __init__(self, brand, model , price):
        self.brand = brand
        self.model = model
        self.price = price
    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model

obj1 = Mobile("Samsung","android",18000)
obj2 = Mobile("Vivo", "android", 20000)
obj3 = Mobile("Apple" , "iphone", 80000)

print(obj1 == obj2)
print(obj2 == obj3)
print(obj1 == obj3)