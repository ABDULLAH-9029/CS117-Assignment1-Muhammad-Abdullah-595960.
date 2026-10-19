def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return (i ** 2) * r
# TEST VALUES
v = 12
r = 6
current = ohms_current(v, r)
power = power_dissipated(current, r)
#PRINT
print(f" Current = { current: .1f} A ")
print(f" Power = { power: .1f} W ")