import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, cities):
    # Verify Requirement 2: Tour must start and end at depot city (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 4: The output should be the list of city indices for the tour starting and ending at the depot city
    # Verify Requirement 1: The robot must visit exactly 8 cities from the provided set of 15 (total of 9 including the starting and ending city)
    if len(tour) != 9:
        return "FAIL"
    
    unique_cities = set(tour)
    # Remove depot city before checking unique city count
    unique_cities.discard(0)
    if len(unique_cities) != 7:
        return "FAIL"
    
    # Calculate the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    # Verify Requirement 5: Check if the reported total travel cost is close to the computed cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Given solution
solution_tour = [0, 4, 12, 2, 6, 11, 8, 1, 0]
solution_total_cost = 103.44135516376741

# Coordinates of cities
cities_coordinates = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99),
}

# Run the verification
test_result = verify_solution(solution_tour, solution_total_cost, cities_coordinates)
print(test_result)