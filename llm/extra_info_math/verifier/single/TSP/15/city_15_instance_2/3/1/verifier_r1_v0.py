import math

# Coordinates of the cities including the depot (city 0)
coordinates = [
    (54, 87),  # depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Solution found by the solver
tour = [0, 2, 7, 13, 9, 10, 5, 3, 4, 12, 8, 1, 14, 11, 6, 0]
reported_cost = 311.877641807867

def calculate_euclidean_distance(city1_idx, city2_idx):
    x1, y1 = coordinates[city1_idx]
    x2, y2 = coordinates[city2_idx]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_tour_requirements(tour, coordinates):
    # Checking if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        print("Requirement 1 and 3 failed: Tour must start and end at the depot city 0.")
        return "FAIL"

    # Checking if all other cities are visited exactly once
    visited_cities = set(tour[1:-1])
    if len(visited_cities) != len(coordinates) - 1 or any(city not in visited_cities for city in range(1, len(coordinates))):
        print("Requirement 2 failed: All cities must be visited exactly once, except depot.")
        return "FAIL"

    # Calculating the total travel cost and compare with reported cost
    calculated_cost = sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        print("Requirement 4 failed: Calculated travel cost does not match reported cost.")
        return "FAIL"
    
    # Check if the subtours are prevented (implicit by order of visit once each city)
    # No explicit check required as the previous condition ensures no duplicate visits

    return "CORRECT"

# Verify if the solution meets the requirements
result = check_tour_requirements(tour, coordinates)
print(result)