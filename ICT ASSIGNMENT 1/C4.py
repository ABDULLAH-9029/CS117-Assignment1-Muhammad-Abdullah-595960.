def loaded_divider(vs, resistor1, resistor2, resistorl):
    # Step 1: Compute parallel equivalent of r2 and rl
    resistor2_parallel_resistorl = (resistor2 * resistorl) / (resistor2 + resistorl)
    
    # Step 2: Unloaded theoretical voltage using original r1 and r2
    unloaded_v = vs * (resistor2 / (resistor1 + resistor2))
    
    # Step 3: Actual loaded voltage using r1 and the parallel combination
    loaded_v = vs * (resistor2_parallel_resistorl / (resistor1 + resistor2_parallel_resistorl))
    
    return (unloaded_v, loaded_v)

print(f"loaded_divider(15, 2000, 2000, 700) -> {loaded_divider(15, 2000,2000, 700)}")