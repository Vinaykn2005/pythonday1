class Payment:
    def pay(self):
        print("The payment is succesful")
class Google(Payment):
    def pay(self):
        print("The payment is Succesfull through Googlepay")
class Phone(Payment):
    def pay(self):
        print("The payment is Succesfull through Phonepay")
class Creditcard(Payment):
    def pay(self):
        print("The payment is succesfull through Criditcard")

ob1 = Google()
ob2 = Phone()
ob3 = Creditcard()
ob1.pay()
ob2.pay()
ob3.pay()
        
    