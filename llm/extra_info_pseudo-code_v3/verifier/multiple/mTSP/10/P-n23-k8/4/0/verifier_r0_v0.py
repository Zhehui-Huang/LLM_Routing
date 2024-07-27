import numpy as np

def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (30, 40), 
    1: (37, 52), 
    2: (49, 49), 
    3: (52, 64), 
    4: (31, 62), 
    5: (52, 33), 
    6: (42, 41), 
    7: (52, 41), 
    8: (57, 58), 
    9: (62, 42), 
    10: (42, 57), 
    11: (27, 68), 
    12: (43, 67), 
    13: (58, 48), 
    14: (58, 27), 
    15: (37, 69), 
    16: (38, 46), 
    17: (61, 33), 
    18: (62, 63), 
    19: (63, 69), 
    20: (45, 35), 
    21: (32, 39), 
    22: (56, 37)
}

robots_tours = [
    [0, 13, 20, 21, 0],
    [0, 19, 5, 15, 0],
    [0, 22, 1, 11, 0],
    [0, 7, 8, 4, 0],
    [0, 2, 10, 14, 0],
    [0, 16, 18, 6, 0],
    [0, 12, 17, 0],
    [0, 3, 9, 0]
]

# Verify that all cities are visited exactly once
visited_cities = set()
for robot_tour in robots_tours:
    for city in robot_tour:
        if city != 0:
            visited_cities.add(city)

# Check if all cities are accounted for
all_cities = set(range(1, 23))
if visited_cities == all_cities:
    verification_result = "CORRECT"
else:
    verification_result = "FAIL"

print(verification_result)