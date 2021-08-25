import random

MINIMUM = 1
MAXIMUM = 45
PER_LINE = 6

def main():
    number = int(input("How many quick picks? "))
    while number < 0:
        print("Invalid Input")
        number = int(input("How many quick picks? "))
    
    
    for i in range(number):
        quick_pick = []
        for j in range(PER_LINE):
            pick = (random.randint(MINIMUM, MAXIMUM))
            while pick in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))

main()

