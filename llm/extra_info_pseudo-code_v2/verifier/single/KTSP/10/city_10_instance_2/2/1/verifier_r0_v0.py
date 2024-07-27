import math

# Given solution
tour = [0, 1, 2, 7, 4, 8, 0]
total_travel_cost = 219

# Coordinates of cities (including the depot)
coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_tour_and_cost(tour, total_travel_cost, coordinates):
    # Check start and end city
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"
    
    # Check number of cities (6 unique cities + 1 repeated depot)
    if len(set(tour)) != 6:
        return "FAIL"

    # Calculate the travel cost from the tour
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    # Check if the total cost matches
    if not math.isclose(computed_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Verify the solution
result = verify_tour_and_cost(tour, total_travel_cost, coordinates)
print(result)