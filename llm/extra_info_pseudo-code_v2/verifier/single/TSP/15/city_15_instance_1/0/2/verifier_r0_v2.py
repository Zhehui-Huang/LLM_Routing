import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, coordinates, total_cost_provided):
    # Check Requirement 1: Starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Every city is visited once, except the depot city which is visited twice
    unique_cities = set(tour[1:-1])  # Exclude the first and last entry (depot)
    if unique_cities != set(range(1, len(coordinates))) or tour.count(0) != 2:
        return "FAIL"

    # Check Requirement 3: Travel cost is calculated using Euclidean distance
    calculated_total_cost = 0
    for i in range(1, len(tour)):
        city1 = tour[i-1]
        city2 = tour[i]
        calculated_total_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])
    
    if not math.isclose(calculated_total_cost, total_cost_provided, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# City coordinates including the depot (index 0)
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Tour provided (output from the algorithm)
tour = [0, 5, 12, 11, 2, 8, 14, 13, 6, 1, 7, 3, 9, 10, 4, 0]
total_cost_provided = 373.4267090803889

# Validation of the tour
result = verify_tour(tour, coordinates, total_cost_provided)
print(result)