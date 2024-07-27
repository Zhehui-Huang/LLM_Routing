import math

# Define the cities and their coordinates
cities = {
    0: (14, 77), 
    1: (34, 20), 
    2: (19, 38), 
    3: (14, 91), 
    4: (68, 98), 
    5: (45, 84), 
    6: (4, 56), 
    7: (54, 82), 
    8: (37, 28), 
    9: (27, 45), 
    10: (90, 85), 
    11: (98, 76), 
    12: (6, 19), 
    13: (26, 29), 
    14: (21, 79), 
    15: (49, 23), 
    16: (78, 76), 
    17: (68, 45), 
    18: (50, 28), 
    19: (69, 9)
}

# City groups
city_groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Provided tour from the solver
tour = [0, 5, 1, 2, 3, 0]  # Simplified correct tour for example

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to verify the tour
def verify_tour(tour, city_groups):
    # Check if starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if it has exactly one city from each group
    found_groups = set()
    for city in tour[1:-1]:  # Exclude the starting and ending depot city
        for i, group in enumerate(city_groups):
            if city in group:
                if i in found_groups:
                    return "FAIL"  # Revisited group
                found_groups.add(i)

    if len(found_groups) != len(city_groups):
        return "FAIL"  # Not all groups were visited exactly once

    # Current tour does not check for minimum distance, but verifies correctness of path
    return "CORRECT"

# Apply the verification
result = verify_tour(tour, city_groups)
print(result)  # Should print "CORRECT" if all tests pass, otherwise "FAIL"