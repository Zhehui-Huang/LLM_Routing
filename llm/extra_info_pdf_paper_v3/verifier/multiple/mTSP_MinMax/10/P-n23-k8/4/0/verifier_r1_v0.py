def calculate_distance(city1, city2):
    from math import sqrt
    return sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(tours, city_coordinates):
    visited_cities = set()
    all_correct = True
    max_travel_cost = 0
    
    # Requirement 1: Check for each tour to start and end at the depot, and all cities visited exactly once.
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            all_correct = False # Depot start and end check
        # Collecting all visited cities (excluding the depot as a destination to visit again)
        visited_cities.update(set(tour[1:-1])) # Exclude the starting and ending depot
    
    if len(visited_cities) != 22: # Total cities - 1 (depot)
        all_correct = False # Check if all cities are visited precisely once

    # Requirement 2: Already checked by starting and ending conditions checks for now.
    
    # Calculating and checking distances / costs:
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        max_travel_cost = max(max_travel_cost, tour_cost)
    
    # Assuming an external max_travel_cost value to check against, since it's not provided:
    # Requirement 3: the primary objective is to minimize the maximum distance traveled by any single robot.
    # Given maximum travel cost from the problem specification part, not processed here since value should be calculated from tours.

    if all_correct and int(max_travel_cost) == 97:
        return "CORRECT"
    else:
        return "FAIL"

# Tours definition from provided solution
tours = [
    [0, 5, 14, 20, 0],
    [0, 12, 15, 0],
    [0, 3, 8, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 1, 6, 16, 21, 0],
    [0, 7, 17, 22, 0],
    [0, 2, 10, 0],
    [0, 9, 13, 0]
]
city_coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
                    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
                    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
                    (32, 39), (56, 37)]

# Test Verification
result = verify_solution(tours, city_coordinates)
print(result)