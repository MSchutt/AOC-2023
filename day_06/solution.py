
from typing import Tuple


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        
    time_row = lines[0].split()
    distance_row = lines[1].split()
    
    assert len(time_row) == len(distance_row)
    
    # Parse the input into a list of races (time, distance)
    races: Tuple[int, int] = [(int(time_row[i]), int(distance_row[i])) for i in range(1, len(time_row))]
    
    number_of_races_beaten = [0] * len(races)
    
    for race_id, (time, distance_to_win) in enumerate(races):
        speed = 0
        # Simulate all the races
        for i in range(time):
            number_of_seconds_charged = i + 1
            speed += 1
            
            # Distance traveled = speed * (time of the race - number of seconds charged)
            distance = speed * (time - number_of_seconds_charged)
            
            if distance > distance_to_win:
                number_of_races_beaten[race_id] += 1
    
    print(number_of_races_beaten)
    
    score = 1
    for race_beaten in number_of_races_beaten:
        score *= race_beaten
        
    print(score)
if __name__ == "__main__":
    main()