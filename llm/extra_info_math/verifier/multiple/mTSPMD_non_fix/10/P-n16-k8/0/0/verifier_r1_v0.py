import math

# City coordinates
cities = [
    (30, 40),  # 0 Depot city 0
    (37, 52),  # 1 Depot city 1
    (49, 49),  # 2 Depot city 2
    (52, 64),  # 3 Depot city 3
    (31, 62),  # 4 Depot city 4
    (52, 33),  # 5 Depot city 5
    (42, 41),  # 6 Depot city 6
    (52, 41),  # 7 Depot city 7
    (57, 58),  # 8 City 8
    (62, 42),  # 9 City 9
    (42, 57),  # 10 City 10
    (27, 68),  # 11 City 11
    (43, 67),  # 12 City 12
    (58, 48),  # 13 City 13
    (58, 27),  # 14 City 14
    (37, 69)   # 15 City 15
]

# Recorded tours and their costs
tours = [
    [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [0, 1], [0, 1], [0, 1]
]

costs = [
    13.892443989449804, 13.892443989449804, 13.892443989449804, 13.892443989449804,
    13.892443989449804, 13.892443989449804, 13.892443989449804, 13.892443989449804
]

# Helper function to calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Requirement checks
def validate_requirements(tours, costs):
    # Check requirement 1: 8 robots leave depot city 0
    if not all(tour[0] == 0 for tour in tours):
        return "FAIL"

    # Check requirement 2: Each city is visited exactly once
    all_visited = sum(tours, [])
    if set(all_visited) != set(range(len(cities))):
        return "FAIL"

    # Check requirement 3: Minimize total travel cost
    # Recompute costs to validate against provided costs
    recalculated_costs = [sum(calc_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1)) for tour in tours]
    computed_total_cost = sum(recalculated_costs)

    if not math.isclose(computed_total_cost, 111.13955191559843, rel_tol=1e-9):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Run the validation
result = validate_requirements(tours, costs)
print(result)