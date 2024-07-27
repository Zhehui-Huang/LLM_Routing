import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(cities, tour, expected_cost):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour consists of exactly 4 cities including the depot city
    if len(tour) != 5:  # Includes the return to the start city
        return "FAIL"

    # Requirement 3: Check for the shortest tour distance calculation using the Euclidean formula
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(total_distance, expected_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# City coordinates indexed by the city number
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Provided solution to test
tour_solution = [0, 8, 10, 11, 0]
expected_cost = 110.01

# Verify the solution tour
print(verify_tour(cities, tour_solution, expected_cost))