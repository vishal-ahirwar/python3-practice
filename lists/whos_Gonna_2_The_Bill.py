print("I'm here to decide who's gonna to pay the bill this time :)")
name =input("Enter names  :")
from random import randint
list_of_name =name.split(",")

print(f"This time {list_of_name[randint(0,len(list_of_name)-1)]} will pay the bill.")
