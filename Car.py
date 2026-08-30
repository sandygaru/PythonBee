class Car:
    def __init__(self,name,color,model,price):
        self.name=name
        self.color=color
        self.model=model
        self.price=price
        
    def display(self):
        print("My car is ", self.name, " of ",self.color, " color")
        print("It is of ",self.model," model of price ",self.price)
        
        
car1 = Car("Thar","Black",2026,1500000)
car2 = Car("Fortuner","White",2022,2000000)

car1.display()
car2.display()