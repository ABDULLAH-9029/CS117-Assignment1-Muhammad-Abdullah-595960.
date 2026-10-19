def decimal_to_binary(n):
    if n == 0:
        return "0"
    #WHILE LOOP
    binary_str = ""
    while n > 0:
        remainder = n % 2
        binary_str = str(remainder) + binary_str
        n = n // 2
    return binary_str
#PRINT
print(f"decimal_to_binary(20) -> {decimal_to_binary(20)}")
print(f"decimal_to_binary(55) -> {decimal_to_binary(55)}")