
class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, directoin):
        return f'\nThe {self.name} turned {directoin}'

    def show_speed(self):
        return f'\nYour speed is {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nYour speed is higher than allow! Your speed is {self.show_speed}'
        else:
            return f'Speed of {self.name} is normal'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'\nSpeed of {self.name} is normal'

class PoliceCar(Car):
    pass

town = TownCar('MINI', 60, 'pink', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('Ferrari', 210, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('VW', 100, 'black', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Ford', 100, 'white', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

