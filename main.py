filename = input("Enter your file name: ")
name = input("Enter your name: ")
address = input("What is your street address: ")
phone = input("Enter your phone number: ")

with open(filename, 'w') as file:
    file.write(f"{name},{address},{phone}")

with open(filename, 'r') as file:
    contents = file.read()
    print(contents)
