#Crops
from Wheat_class import *
from Potato_class import *

def DisplayMenu():
  print()
  print("Which crop do you want?: ")
  print()
  print("1. Potato")
  print("2. Wheat")
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

def create_crop():
  DisplayMenu()
  choice = selectOption()
  if choice == 1:
    new_crop = Potato()
  elif choice == 2:
    new_crop = Wheat()
  return new_crop

def main():
  new_crop = create_crop()
  manageCrop(new_crop)

if __name__ == "__main__":
  main()
