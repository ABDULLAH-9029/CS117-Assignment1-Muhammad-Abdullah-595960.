readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
above_3_2 = 0
total_sum = 0
count = 0
#highest and lowest readings
highest = readings[0]
lowest = readings[0]
#if
for val in readings:
    if val > 3.2:
        above_3_2 += 1
    if val > highest:
        highest = val
    if val < lowest:
        lowest = val
    total_sum += val
    count += 1
#average
average = total_sum / count
#print
print(f"Readings above 3.2 V: {above_3_2}")
print(f"Highest: {highest} V")
print(f"Lowest: {lowest} V")
print(f"Average: {average:.2f} V")