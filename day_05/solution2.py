from typing import Dict, Tuple, List
from time import time

def get_mapped_value(conversion_maps: Dict[str, Dict[str, List[int]]], source: str, destination: str, value: int) -> int:
    """ Given a conversion map, source, destination, and value, return the mapped value


    Args:
        conversion_maps (Dict[str, Dict[str, Tuple): Conversion Map
        source (str): Source
        destination (str): Target
        value (int): value to convert

    Returns:
        int: mapped value
    """
    
    # Iterate through the mapping ranges and find the correct one
    mapping_range = conversion_maps[source][destination]
    for dest, start, range_len in mapping_range:
        # Check if within the range
        if value >= start and value < start + range_len:
            mapping_difference = dest - start
            # Map the value; dest -> destination range; start -> source range
            return value + mapping_difference
    return value
            

def main():
    with open("input.txt") as f:
        data = f.read().strip().splitlines()
        
    
    # -> stores source -> 
    conversion_maps: Dict[str, Dict[str, Tuple(int, int, int)]] = {}
    

    init_seeds = [int(x) for x in data[0].split(" ")[1:]]
    seeds = []
    for i in range(0, len(init_seeds), 2):
        start = init_seeds[i]
        rang = init_seeds[i + 1]
        seeds.extend(range(start, start + rang))
    
    last_row = True
    current_source = ""
    current_destination = ""
    
    for row in data[2:]:
        # Empty row symbolizes that the next mapping is coming up
        if not row:
            last_row = True
            continue
        if last_row:
            last_row = False
            row = row.replace(" map:", "").split("-to-")
            current_source = row[0]
            current_destination = row[1]
            if current_source not in conversion_maps:
                conversion_maps[current_source] = {}
            if current_destination not in conversion_maps[current_source]:
                conversion_maps[current_source][current_destination] = []
        else:
            # parse the range mapping
            dest, start, range_len = row.split(" ")
            conversion_maps[current_source][current_destination].append((int(dest), int(start), int(range_len)))
    
    # Brute force :>
    # 11554135
    print(get_min_location(seeds, conversion_maps=conversion_maps))


def get_min_location(seeds: List[int], conversion_maps: Dict[str, Dict[str, List[int]]]):
    print(f"Brute Forcing a total of {len(seeds)} seeds")
    start = time()
    one_percent = 16_000_000
    min_loc = 10000000000
    for i, seed in enumerate(seeds):
        if i % one_percent == 0:
            print(f"{i // one_percent}% done. Time elapsed: {time() - start}")
        seed_val = seed
        source = "seed"
        target = list(conversion_maps[source].keys())[0]
        while target is not None:
            seed_val = get_mapped_value(conversion_maps, source, target, seed_val)
            source = target
            target = list(conversion_maps[source].keys())[0] if source in conversion_maps else None
        if seed_val < min_loc:
            min_loc = seed_val
    return min_loc

if __name__ == '__main__':
    main()