#CHECKING OHMS LAW

voltage=float(input("Enter voltage:"))
resistance=input("Enter resistance")
if resistance <0:
    print("invalid resistance")
else:
    I = voltage / resistance
    print(f"Current = {I: .1f} A", )
    if I > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
    