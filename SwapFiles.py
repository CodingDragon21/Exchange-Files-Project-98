
def swapFiles():
    input1 = input("Name of File 1: ")
    input2 = input("Name of File 2: ")
    
    with open(input1, "r") as a:
        data_a = a.read()

    with open(input2, "r") as b:
        data_b = b.read()

    with open(input1, "w") as a:
        a.write(data_b)

    with open(input2, "w") as b:
        b.write(data_a)

print("Exchanges has been successful!")

swapFiles()

