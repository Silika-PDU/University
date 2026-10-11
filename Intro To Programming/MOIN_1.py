highest_number = None

while True:
    user_number = input("enter a number or type 'done' to end: ")
    if user_number.lower() == "done":
        break
    
    num = int(user_number)
    
    if highest_number is None or num > highest_number:
        highest_number = num

print(highest_number)
