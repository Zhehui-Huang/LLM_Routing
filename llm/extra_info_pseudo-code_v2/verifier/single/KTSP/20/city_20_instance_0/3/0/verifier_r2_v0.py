import numpy as np

# Define the city locations
city_coordinates = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Provided solution
solution_tour = [0, 19, 6, 10, 0]
solution_cost = 207.87

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, calculated_cost):
    # Check requirement 1: Tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check requirement 2: Visit exactly 4 cities including the depot
    if len(tour) != 5:
        return "FAIL"
    if len(set(tour)) != 5:  # including repetitions, ensuring exactly 4 unique cities plus depot
        return "FAIL"
    
    # Check requirement 5: Output is in correct format with correct cost
    expected_cost = 0
    for i in range(len(tour) - 1):
        expected_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
    
    if not np.isclose(expected_cost, calculated_cost, atol=0.01):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Run the verification
result = verify_solution(solution_tour, solution_cost)
print(result)