from itertools import cycle

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
        
    
    current_position = "AAA"
    
    number_of_steps = 0
    
    # Cycle the instructions until ZZZ is found
    for instruction in cycle(instructions):
        number_of_steps += 1
        current_position = matrix[current_position][0] if instruction == "L" else matrix[current_position][1]
        if current_position == "ZZZ":
            break
        
    # 11567
    print(number_of_steps)


if __name__ == "__main__":
    main()