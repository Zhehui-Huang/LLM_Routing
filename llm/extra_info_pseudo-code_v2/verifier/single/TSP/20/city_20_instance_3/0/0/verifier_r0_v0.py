import math

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Coordinates for each city
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Proposed solution
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
reported_cost = 458.36719998557066

# Verify the requirements
def verify_solution(tour, reported_cost, coordinates):
    # Requirement 2 and 6
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 19 or set(range(1, 20)) != unique_cities:
        return "FAIL"
    
    # Requirement 4 and 7
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    # Requirement 7 (check if costs are close enough)
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_solution(tour, reported_cost, coordinates)
print(result)