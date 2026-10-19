count1 = 0
count5 = 0
count_out = 0

while True:
    r = float(input("Enter resistance (0 to stop): "))

    if r == 0:
        break

    if 99 <= r <= 101:
        count1 += 1
    elif 95 <= r <= 105:
        count5 += 1
    else:
        count_out += 1

print("1% tolerance:", count1)
print("5% tolerance:", count5)
print("Out of tolerance:", count_out)
