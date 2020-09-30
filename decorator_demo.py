class Car:
    def __init__(self,name,price):
        self._name = name
        self._price = price

    @property
    def car_name(self):
        return self._name

    @car_name.setter
    def car_name(self, value):
        self._name = value


    @property
    def car_price(self):
        return str(self._price) + "万"

benz = Car("benz", 30)

print(benz.car_name)
benz.car_name = "baojun"
print(benz.car_name)
print(benz.car_price)
