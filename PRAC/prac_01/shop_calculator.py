total = 0
no_items = int(input("Number of Items: ")) 
while no_items <= 0:
    print("Invalid Number of items!")
    no_items = int(input("Number of Items: ")) 
for i in range(no_items):
    price = float(input("Price of item: "))
    total += price

if total > 100: 
    total * 0.9 

print("Total price for ", no_items, " items is $", total, sep='')

