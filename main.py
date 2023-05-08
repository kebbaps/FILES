filename = input("What is your file name: ")
name = input("What is your name: ")
address = input("What is your street address: ")
phone = input("What is your phone number: ")

with open(filename, 'w') as file:
    file.write(f"{name},{address},{phone}")

with open(filename, 'r') as file:
    contents = file.read()
    print(contents)
