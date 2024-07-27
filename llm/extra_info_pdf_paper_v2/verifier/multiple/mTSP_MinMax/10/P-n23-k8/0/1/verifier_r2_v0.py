import math
from itertools import chain

# Constants and data
num_cities = 23  # includes depot
num_robots = 8

# Coordinates corresponding to city indices 0 (depot), 1 through 22
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Provided tours by the robot (user solution)
robot_tours = [
    [0, 21, 22, 17, 7, 13, 2, 1, 4, 11, 0],
    [0, 15, 10, 12, 18, 19, 3, 8, 0],
    [0, 20, 14, 5, 9, 0],
    [0, 16, 6, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
]

# Function to calculate euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Verify that all tours start and end at depot, and all cities are visited exactly once
def verify_tours(robot_tours, coordinates):
    cities_visited = list(chain.from_iterable(tour[1:-1] for tour in robot_tours))
    unique_cities_visited = set(cities_visited)
    
    # Check all cities are visited
    if unique_cities_visited != set(range(1, len(coordinates))):  # Exclude depot
        return "FAIL: Not all cities were visited."
    
    # Check each tour starts and ends at the depot
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Not all tours start and end at the depot."
    
    # Verify number of cities including the depot 
    # and excluding multiple 0's mistakenly placed within the tours
    if sorted(cities_visited + [0]) != sorted(range(len(coordinates))):
        return "FAIL: City indices mismatch or improperly visited."
    
    return "CORRECT"

# Retrieve verification output
result = verify_tours(robot_tours, coordinates)
print(result)