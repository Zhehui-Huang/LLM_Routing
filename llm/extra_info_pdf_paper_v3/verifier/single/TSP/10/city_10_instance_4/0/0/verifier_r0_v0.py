import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_solution(tour, total_cost, coordinates):
    # Decompose coordinates for easier use
    depot = coordinates[0]
    cities = coordinates[1:]

    # [Requirement 1] Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit other cities exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) or any(c not in range(1, len(coordinates)) for c in unique_cities):
        return "FAIL"

    # [Requirement 4] Output includes the tour from the depot and back
    # Requirement is already implicitly checked by the lists provided

    # [Requirement 3 & 5] Calculate the total distance and compare with given total cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])

    if abs(computed_cost - total_cost) > 1e-6:  # Use a small tolerance for floating point comparison
        return "FAIL"

    return "CORRECT"

# Coordinates of the cities
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Proposed solution
proposed_tour = [0, 3, 6, 3, 0, 4, 0]
proposed_total_cost = 150.82407304373584

# Verify the solution
result = verify_solution(proposed_tour, proposed_total_cost, coordinates)
print(result)