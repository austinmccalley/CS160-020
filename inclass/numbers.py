# Largest number being able to represented by x amount of bits

bits=input("How many bits do you want? ")
bits=int(bits)

print("The largest number represented by " + str(bits) + " bits is " + str((2**bits)-1) +".")
