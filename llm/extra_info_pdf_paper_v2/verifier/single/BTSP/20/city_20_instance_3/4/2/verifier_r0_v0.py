import numpy as np
import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def check_tour(tour, distances):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city 0."
    if sorted(tour) != sorted(list(range(20))):
        return "FAIL: Tour does not visit each city exactly once."
    max_dist = 0
    for i in range(len(tour) - 1):
        max_dist = max(max_dist, distances[tour[i]][tour[i+1]])
    if max_dist > 68.15:
        return f"FAIL: Longest distance between any two consecutive cities is higher than expected. Found: {max_dist} > 68.15"
    return "CORRRECT"

def unit_test_solution():
    cities = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
        5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 
        10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
        15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }

    # Generate distances matrix
    distances = np.zeros((20, 20))
    for i in range(20):
        for j in range(20):
            if i != j:
                distances[i][j] = calculate_distance(cities[i], cities[j])
            else:
                distances[i][j] = 0

    # Provided tour including solution validation
    tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
    result = check_tour(tour, distances)
    print(result)

unit_test_solution()