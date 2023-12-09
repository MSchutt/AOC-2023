from itertools import cycle
from math import lcm

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        
    instructions = lines[0].strip()
    
    matrix = {}
    # Can skip row 1 -> whitespace
    for row in lines[2:]:
        key, mapping = row.split("=")
        key = key.strip()
        
        mapping = mapping.replace("(", "").replace(")", "").split(",")
        left_mapping = mapping[0].strip()
        right_mapping = mapping[1].strip()
        
        matrix[key] = (left_mapping, right_mapping)
        
    
    positions = [key for key in matrix.keys() if key.endswith("A")]
    
    number_of_steps = 0
    
    results = []
    
    # After verifying that the input indeed has a cycle, LCM can be used to find the number of steps
    # So try to find the number of steps required until a step that ends in Z is found and store the number of required steps
    # After that's finished for all positions, just call LCM to find the least common multiplier === the number of steps required until all positions end in Z!
    
    for instruction in cycle(instructions):
        number_of_steps += 1
        # Move the positions
        positions = [matrix[position][0] if instruction == "L" else matrix[position][1] for position in positions]
        
        # Check if any of the positions end in Z
        for position in positions:
            if position.endswith("Z"):
                results.append(number_of_steps)
        # After finished -> remove all positions that end in Z (no longer needed)
        positions = [position for position in positions if not position.endswith("Z")]
        if len(positions) == 0:
            break
                
    print(results)
    
    # 9858474970153
    print(lcm(*results))


if __name__ == "__main__":
    main()