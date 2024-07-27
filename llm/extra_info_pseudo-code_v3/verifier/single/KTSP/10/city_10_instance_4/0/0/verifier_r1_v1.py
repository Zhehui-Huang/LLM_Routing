import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_solution():
    cities_coordinates = [
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

    proposed_tour = [0, 4, 5, 1, 9, 8, 2, 3, 0]
    proposed_cost = 272.21

    # Check requirement: Starts and ends at depot city 
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Check requirement: Exactly 8 cities visited (including depot city)
    if len(set(proposed_tour)) != 9:  # 8 unique cities + 1 depot repeated
        return "FAIL"

    # Check requirement: Total travel cost calculation
    calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        calculated_cost += calculate_distance(cities_coordinates[proposed_tour[i]], cities_coordinates[proposed_tour[i+1]])

    # Check if calculated cost is approximately equal to the proposed cost (allowing for slight floating-point errors)
    if not math.isclose(calculated_cost, proposed_cost, rel_tol=1e-3):
        return "FAIL"

    # Test passed all checks
    return "CORRECT"

result = test_solution()
print(result)