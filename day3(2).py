class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
    def display_product(self):
        print("product name and price", self.product_name,self.price)
    
class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty
    def display_electronic_product(self):
        print("brand and warranty", self.brand,self.warranty)
     
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage
    def display_mobile_details(self):
        print("RAM and Storage", self.ram,self.storage)
    
vivo = MobilePhone("VIVOY56","18K","VIVO","1 year","8GB","128GB")
vivo.display_mobile_details()
vivo.display_electronic_product()
vivo.display_mobile_details()