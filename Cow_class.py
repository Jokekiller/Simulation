#Cow class
from Animal_class import *

class Cow(Animal):
  """A cow """
  #constructor
  def __init__(self):
    super().__init__(1,7,8)
    self._type = "Cow"
    self._name = "Bettsy"

  def grow(self, food, water):
    if food >= self._food_need and water >= self._water_need:
      if self._status == "Baby" and water > self._water_need:
        self._weight += self._growth_rate * 1.5
      elif self._status == "Young" and water > self._water_need:
        self._weight += self._growth_rate * 1.35
      else:
        self._weight += self._growth_rate
    self._days_growing += 1
    self._update_status()

def main():
  cow_animal = Cow()
  print(cow_animal.report())
  manual_grow(cow_animal)
  print(cow_animal.report())
  manual_grow(cow_animal)
  print(cow_animal.report())

if __name__ == "__main__":
  main()
