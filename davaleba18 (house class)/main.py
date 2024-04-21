class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"სახელი: {self.name}, Deposit: {self.deposit}, სესხი: {self.loan}"

class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "იყიდება"

    def __str__(self):
        return f"ID: {self.ID}, ფასი: {self.price}, მფლობელი: {self.owner.name}, სტატუსი: {self.status}"

    def sell(self, buyer, loan=0):
        if loan == 0:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "გაყიდულია"
            print(f"The house with ID {self.ID} has been sold to {buyer.name}.")
        else:
            self.owner = buyer
            self.status = "გაყიდული სესხით"
            buyer.loan += loan
            print(f"The house with ID {self.ID} has been sold to {buyer.name} with a loan of {loan}.")


owner = Person("Owner")
buyer = Person("Buyer")
house = House("0123456789", 200000, owner)

print("Before sale:")
print(owner)
print(buyer)
print(house)


print("\nAfter sale:")
house.sell(buyer)
print(owner)
print(buyer)
print(house)


print("\nAfter sale on loan:")
house.sell(buyer, loan=150000)
print(owner)
print(buyer)
print(house)

