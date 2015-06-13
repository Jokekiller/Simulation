#Sheep class
from Animal_class import *

class Sheep(Animal):
  """A Sheep"""
  #constructor
  def __init__(self):
    super().__init__(1,5,6)
    self._type = "Sheep"
    self._name = "Dave"

  def grow(self, food, water):
    if food >= self._food_need and water >= self._water_need:
      if self._status == "Baby" and water > self._water_need:
        self._weight += self._growth_rate * 1.2
      elif self._status == "Young" and water > self._water_need:
        self._weight += self._growth_rate * 1.15
      else:
        self._weight += self._growth_rate
    self._days_growing += 1
    self._update_status()

def main():
  sheep_animal = Sheep()
  print(sheep_animal.report())
  manual_grow(sheep_animal)
  print(sheep_animal.report())
  manual_grow(sheep_animal)
  print(sheep_animal.report())

if __name__ == "__main__":
  main()
      
