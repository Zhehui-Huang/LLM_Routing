import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_tour(tour, cities, expected_cost):
    # Requirement 1: Start and end at the depot city (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Exactly 7 cities visited including the depot.
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Calculate the travel cost and compare with expected cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    # Requirement 3: Check if the calculated cost is close to the expected cost
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define cities coordinates
cities = [
    (84, 67),  # City 0 - Depot
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Given solution
tour = [0, 7, 1, 2, 4, 3, 8, 0]
expected_cost = 166.4224633763765

# Validate the tour
result = validate_tour(tour, cities, expected_cost)
print(result)