class Car:
    total_cars = 0

    def __init__(self, make, model, year):
        self._make = None
        self._make = make
        self._model = model
        self._year = year
        Car.total_cars += 1

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        self._year = year

    def __str__(self):
        return f"Car made by {self._make}, model is {self._model}, produced in {self._year}"

    @classmethod
    def print_count(cls):
        print(cls.total_cars)


car1 = Car(1, 2, 3)
car2 = Car(1, 2, 4)
car3 = Car(1, 2, 5)
car4 = Car(1, 2, 3)
Car.print_count()
