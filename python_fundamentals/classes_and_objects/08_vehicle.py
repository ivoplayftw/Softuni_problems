class Vehicle:
    def __init__(self, type: str, model: str, price:int, owner = None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner
    
    def buy(self, money:int, owner_name:str):
        if money >= self.price and self.owner == None:
            change = money - self.price
            self.owner = owner_name
            return f"Successfully bought a {self.type}. Change: {change:.2f}" 
        elif money < self.price:
            return "Sorry, not enough money"
        elif self.owner != None:
            return "Car already sold"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        else:
            self.owner = None
            
    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
        
        
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
