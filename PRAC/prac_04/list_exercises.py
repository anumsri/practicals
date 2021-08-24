
numbers = []
maxLengthList = 5
while len(numbers) < maxLengthList:
    user_number = int(input("Number: "))
    numbers.append(user_number)
print(f"The First number is {numbers[0]}")
print(f"The Last number is {numbers[-1]}")
print("The Smallest number is", (min(numbers)))
print("The Largest number is", (max(numbers)))
print("The Average of the number is", sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'] 

get_username = str(input("Enter Username: "))
if get_username in usernames:
    print("Access Granted")
else:
    print("Access Denied")