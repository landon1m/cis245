class Car():
    _year_model = ""
    _make = ""
    speed = int

    def __init__(_year_model, _make):
        self._year_model = _year_model
        self._make = _ake
        speed = 0
        
    def accelerate():
        self.speed = self.speed +5
    def brake():
        self.speed = self.speed-5
        if self.speed <0:
            self.speed = 0
    def get_speed():
        print(self.speed)
        return self.speed

car1 = Car(2021,"Tesla")
car.accelerate()
car.get_speed()
