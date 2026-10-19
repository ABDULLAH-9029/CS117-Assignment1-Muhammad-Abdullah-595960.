def parallel_resistance(resistors):
    inverse_sum = 0
    for resistance in resistors:
        inverse_sum += 1 / resistance
    return 1/inverse_sum
#PRINT
print( f"parallel_resistance([20, 20]) -> {parallel_resistance([20, 20])}" )
print( f"parallel_resistance([250, 500, 750]) -> {parallel_resistance([250, 500, 750]):.2f}" )