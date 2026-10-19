num = int(input("How many resistors? "))
total_resistance = 0
for i in range(1, num + 1):
    r = float(input(f"Enter R{i}: "))
    total_resistance += r

print(f"Total resistance = {int(total_resistance)} ohm")