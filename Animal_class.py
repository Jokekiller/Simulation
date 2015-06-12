#Animal class
import random

class Animal:
    """A generic animal"""

    #constructor
    def __init__(self, growth_rate, water_nedd, food_need):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self._name = "Aunik"

    def need(self):
        return {'water_need': self._water_need, 'food need':self._food_need}

    def report(self):
        return {'type':self._type, 'status':self._status, 'Weight':self._weight, 'days growing':self._days_growing}

    def _update_status(self):
        if self._weight > 20:
            self._status = 'Death awaits'
        elif self._weight > 15:
            self._status = 'Getting on a bit'
        elif self._weight > 10:
            self._status = 'Prime time'
        elif self._weight > 5:
            self._status = 'Slightly young'
        elif self._weight > 0:
            self._status = 'Young'
        elif self._weight == 0:
            self._status = 'Baby'

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

def auto_grow(animal, days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food. water)
        
def manual_grow(animal):
    valid = False
    while not valid:
        try:
            food = int(input"Please enter a food value(1-10): "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Value entered not valid - enter a valid value")
        except ValueError:
            print("Value entered not valid - enter a valid value")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value(1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - enter a valid value")
        except ValueError:
            print("Value entered not valid - enter a valid value")
    animal.grow(food, water)

def displayMenu():
    print()
    print("1. Grow manually over 1 day")
    print("2. Grow automatically over 30 days")
    print("3. Report status")
    print("0. Exit test program")
    print()
    print("Please enter a value from the menu: ")

def GetMenuChoice():
    valid = False
    while not valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manageAnimal(animal):
    print("This is the animal management menu")
    print()
    noexit = True
    while noexit:
        displayMenu()
        option = GetMenuChoice()
        print()
        if option == 1:
