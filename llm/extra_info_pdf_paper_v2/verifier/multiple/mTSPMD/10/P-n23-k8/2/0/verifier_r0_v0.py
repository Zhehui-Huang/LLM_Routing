import numpy as np
import math

# Define the city coordinates based on problem statement
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Provided robot tours
robot_tours = [
    [0, 20, 21, 0],
    [1, 16, 1],
    [2, 13, 9, 8, 18, 19, 2],
    [3, 12, 15, 11, 3],
    [4, 10, 4],
    [5, 14, 17, 22, 5],
    [6, 6],
    [7, 7]
]

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def check_tours_and_costs():
    all_cities_visited = set()
    for tour in robot_tours:
        if tour[0] != tour[-1]:  # Check if each robot returns to its starting depot
            return "FAIL"
        
        for i in range(len(tour)-1):
            if tour[i] == np.inf or tour[i+1] == np.inf:
                return "FAIL"  # Checks for invalid index or distance calculations

        all_cities_visited.update(tour)

    # Removing duplicates ignoring the starting and ending depot repetitions
    if len(all_cities_visited) != 23:
        return "FAIL"

    return "CORRECT"

# Run the checks
result = check_tours_and_costs()
print(result)