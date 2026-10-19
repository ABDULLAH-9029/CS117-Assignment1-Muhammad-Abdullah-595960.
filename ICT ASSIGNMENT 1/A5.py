resistance1 = float(input("ENTER RESISTANCE R1: "))
resistance2 = float(input("ENTER RESISTANCE R2: "))
resistance3 = float(input("ENTER RESISTANCE R3: "))

# Find smallest
if resistance1 <= resistance2 and resistance1 <= resistance3:
    smallest = resistance1
elif resistance2 <= resistance1 and resistance2 <= resistance3:
    smallest = resistance2
else:
    smallest = resistance3

# Find largest
if resistance1 >= resistance2 and resistance1 >= resistance3:
    largest = resistance1
elif resistance2 >= resistance1 and resistance2 >= resistance3:
    largest = resistance2
else:
    largest = resistance3

print(f"Smallest = {int(smallest)} ohm")
print(f"Largest = {int(largest)} ohm")