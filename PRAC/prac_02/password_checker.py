"""
Replace the contents of this module docstring with your own details
Name: Arpisitt
Date started: 22/08/21
GitHub URL:https://github.com/cp1404-students/a1-travel-tracker-anumsri
"""
MENU = """L - List Places
R - Recommend random place
A - Add new place
M - Mark a place as visited
Q - Quit"""

import csv

inputfile = csv.reader(open('places.csv', 'r'))

def get_totalplaces():
    num_places = 0
    for row in open("places.csv"):
        num_places += 1
    return num_places

def main():
    print("Travel Tracker 1.0 - by Arpisitt Numsri")
    num_places = get_totalplaces()
    print("{} places loaded from {}".format(num_places, "places.csv"))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            for row in inputfile:
                print(row[1])
#     # # list of all the places with their details and the number of places left to visit [4]
#     #     elif choice == "R":
#     # # display a random choice from any available unvisited places
#     #     elif choice == "A":
#     # # prompt for the place’s name, country and priority, error-checking each of these [3], then add the place to the list in memory (not to the file);
#     #     elif choice == "M":
#     # # : display the list of all places (same as for the list option), then allow the user to choose one place (error-checked), then change that place to visited
#     #     else:
#     #         print("Invalid Menu Choice")
#     #     print(MENU)
#     #     choice = input(">>> ").upper()

if __name__ == '__main__':
    main()