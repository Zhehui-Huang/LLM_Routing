import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tsp_solution():
    cities = [
        (30, 56),  # Depot: City 0
        (53, 42),  # City 1
        (1, 95),   # City 2
        (25, 61),  # City 3
        (69, 57),  # City 4
        (6, 58),   # City 5
        (12, 84),  # City 6
        (72, 77),  # City 7
        (98, 95),  # City 8
        (11, 0),   # City 9
        (61, 25),  # City 10
        (52, 0),   # City 11
        (60, 95),  # City 12
        (10, 94),  # City 13
        (96, 73),  # City 14
        (14, 47),  # City 15
        (18, 16),  # City 16
        (4, 43),   # City 17
        (53, 76),  # City 18
        (19, 72)   # City 19
    ]

    proposed_solution_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 14, 8, 12, 18, 0]
    proposed_solution_cost = 425.9972169790246

    # Check every city except the depot is visited exactly once
    if sorted(proposed_solution_tour[1:-1]) != list(range(1, 20)):
        return "FAIL"

    # Check tour starts and ends at the depot
    if proposed_solution_tour[0] != 0 or proposed_solution_tour[-1] != 0:
        return "FAIL"

    # Calculate the actual travel cost of the provided tour
    total_cost = 0.0
    for i in range(len(proposed_solution_tour) - 1):
        city_a = cities[proposed_solution_tour[i]]
        city_b = cities[proposed_solution_tour[i + 1]]
        total_cost += euclidean_distance(city_a, city_b)

    # Check if the calculated cost is close enough to the reported cost (due to potential floating-point inaccuracies)
    if not math.isclose(total_cost, proposed_solution_cost, rel_tol=1e-9):
        return "FAIL"

    # If all checks passed, return "CORRECT"
    return "CORRECT"

# Running the test function
print(test_tsp_solution())