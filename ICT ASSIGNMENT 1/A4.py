#LOGIC GATES

A = int(input("Enter A: "))
B = int(input("Enter B: "))

if A in (0, 1) and B in (0, 1):
    print("AND =", A & B)
    print("OR =", A | B)
    print("XOR =", A ^ B)
else:
    print("Bits must be 0 or 1")