def star_to_delta(resistora, resistorb, resistorc):
    # Calculate the numerator factor first
    r_numerator = (resistora * resistorb) + (resistorb * resistorc) + (resistorc * resistora)
    
    # Calculate the three Delta resistors
    resistor_ab = r_numerator / resistorc
    resistor_bc = r_numerator / resistora
    resistor_ca = r_numerator / resistorb
    
    # Return rounded values to two decimal places
    return (round(resistor_ab, 2), round(resistor_bc, 2), round(resistor_ca, 2))

print(f"star_to_delta(20,40,60) -> {star_to_delta(20,40,60)}")