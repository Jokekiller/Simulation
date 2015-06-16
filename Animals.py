#Animals
from Cow_class import *
from Sheep_class import *

def DisplayMenu():
  print()
  print("Which animal do you want?: ")
  print()
  print("1. Cow")
  print("2. Sheep")
  print()
  print("Please select an option: ")

def selectOption():
  valid = False
  while not valid:
    try:
      choice = int(input("Option selected: "))
      if choice in (1,2):
        valid = True
      else:
        print("Please enter a valid option")
    except ValueError:
      print("Please enter a valid option")
  return choice

def create_animal():
  DisplayMenu()
  choice = selectOption()
  if choice == 1:
    new_animal = Cow()
  elif choice == 2:
    new_animal = Sheep()
  return new_animal

def main():
  new_animal = create_animal()
  manageAnimal(new_animal)

if __name__ == "__main__":
  main()
    
