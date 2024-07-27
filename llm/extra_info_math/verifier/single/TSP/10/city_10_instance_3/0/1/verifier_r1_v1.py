import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def test_solution(cities, tour, reported_cost):
    # [Requirement 1] and [Requirement 7]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] - Visit each city once except depot
    if len(set(tour)) != len(cities) or set(tour) != set(range(len(cities))):
        return "FAIL"

    # [Requirement 3] - Starts and ends at depot (checked implicitly with R1 & R7)
    
    # [Requirement 4] & [Requirement 8] - Accurate travel cost calculation and reporting
    calculated_cost = calculate_total_travel_haul_cost(cities, tour)
    if abs(calculated_cost - reported_cost) > 0.001:  # Allowing a small error margin
        return "FAIL"

    # [Requirement 5] - Minimization of the tours cost by method cannot be tested directly here.

    # [Requirement 6] - Subtour elimination, assumed managed by solution method

    return "CORRECT"

# Define cities coordinates. Assuming they are given as:
cities = [
    (84, 67),  # Depot city 0
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

# Initially reported tour and cost
tour = [0, 7, 1, 4, 2, 5, 6, 9, 3, 8, 0]
reported_cost = 294.17253892411236

# Now run the test with the fixed function
print(test_solution(cities, tour, reported_cost))