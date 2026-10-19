readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
#READING ABOBE 3.2
above_3_2 = 0
total_sum = 0
count = 0
#HIGHEST READING
highest = readings[0]
#LOWEST READING
lowest = readings[0]
#FOR LOOP:
for val in readings:
    if val > 3.2:
        above_3_2 += 1
    if val > highest:
        highest = val
    if val < lowest:
        lowest = val
    total_sum += val
    count += 1
#AVERAGE
average = total_sum / count
#PRINT 
print(f"Readings above 3.2 V: {above_3_2}")
print(f"Highest: {highest} V")
print(f"Lowest: {lowest} V")
print(f"Average: {average:.2f} V")