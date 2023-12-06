
from typing import Tuple


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        
    time_row = lines[0].replace("Time:", "").replace(" ", "").strip()
    distance_row = lines[1].replace("Distance:", "").replace(" ", "").strip()
    

    time = int(time_row)
    distance_to_win = int(distance_row)

    races_beaten = 0
    
    print(f"Time: {time}, Distance to win: {distance_to_win}")
    
    speed = 0
    # Simulate all the races
    for i in range(time):
        number_of_seconds_charged = i + 1
        speed += 1
        
        # Distance traveled = speed * (time of the race - number of seconds charged)
        distance = speed * (time - number_of_seconds_charged)
        
        if distance > distance_to_win:
            races_beaten += 1
    
    print(races_beaten)
    
if __name__ == "__main__":
    main()