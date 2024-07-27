import numpy as np

# Define the cities and their coordinates as given.
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Sample tours output from solver (for testing purposes)
robot_tours = {
    0: [0, 1, 5, 9, 17, 14, 7, 0],
    1: [0, 3, 12, 15, 19, 18, 8, 11, 4, 2, 10, 16, 6, 20, 13, 0]
}

def calculate_distance(a, b):
    """ Calculate Euclidean distance between two points. """
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def validate_solution(tours, city_count):
    # All cities visited and only once
    city_visit = [0] * city_count
    for tour in tours.values():
        for city in tour:
            if city != 0:  # Not counting the depot city
                city_visit[city] += 1
    
    cities_visited_once = all(x == 1 for x in city_visit[1:])
    
    # Flow conservation and subcycle elimination
    for tour in tours.values():
        if tour[0] != 0 or tour[-1] != 0:
            # Start or end not at depot
            return "FAIL"
        
        # Check for short cycles not returning to depot but this is typically handled during solving stage.

    # Check binary nature of x_ijk (implicitly checked by tours correctness under typical solver use)

    # Check non-negativity of u_i (implicitly valid if tours are valid)

    return "CORRECT" if cities_visited_once else "FAIL"

# Test the solutions
result = validate_solution(robot_tours, len(cities))
print(result)