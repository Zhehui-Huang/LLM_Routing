import numpy as np
import math

# Given coordinates for the cities including depots
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35)
}

# Given solution
final_tour = [0, 16, 2, 7, 6, 20, 5, 14, 17, 9, 13, 8, 18, 19, 3, 12, 15, 11, 4, 10, 1, 0]
actual_cost = 186.80

# Utility to calculate the Euclidean distance between two points
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Validate the solution
def validate_tour(tour, expected_cost):
    # Check if all cities are visited exactly once and the tour starts and ends at depots
    unique_cities_visited = set(tour)
    if len(unique_cities_visited) != len(coordinates) or tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Calculate the total travel cost
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(tour[i - 1], tour[i])

    # Check if the total calculated cost is close to the expected cost (float precision handled with round)
    if round(total_cost, 2) != expected_cost:
        return False
    
    return True

# Verify that the provided solution meets all the requirements
if validate_tour(final_tour, actual_cost):
    print("CORRECT")
else:
    print("FAIL")