import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # Given city coordinates where index represents the city number
    cities = [
        (14, 77), # City 0 (depot)
        (34, 20), # City 1
        (19, 38), # City 2
        (14, 91), # City 3
        (68, 98), # City 4
        (45, 84), # City 5
        (4, 56),  # City 6
        (54, 82), # City 7
        (37, 28), # City 8
        (27, 45), # City 9
        (90, 85), # City 10
        (98, 76), # City 11
        (6, 19),  # City 12
        (26, 29), # City 13
        (21, 79), # City 14
        (49, 23), # City 15
        (78, 76), # City 16
        (68, 45), # City 17
        (50, 28), # City 18
        (69, 9)   # City 19
    ]

    # Group information
    groups = [
        [5, 6, 7, 11, 17],
        [1, 4, 8, 13, 16],
        [2, 10, 15, 18, 19],
        [3, 9, 12, 14]
    ]

    # Solution provided
    proposed_tour = [0, 6, 2, 13, 9, 0]
    proposed_cost = 108.66296159815982

    # Check tour starts and ends at the depot
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Check one city from each group is visited
    visited = set(proposed_tour) - {0} # remove the depot
    for group in groups:
        if not visited.intersection(set(group)):
            return "FAIL"
        if len(visited.intersection(set(group))) > 1:
            return "FAIL"

    # Check the travel cost
    actual_cost = 0.0
    for i in range(len(proposed_tour) - 1):
        actual_cost += calculate_distance(cities[proposed_tour[i]], cities[proposed_tour[i+1]])

    if not math.isclose(actual_cost, proposed_cost, abs_tol=1e-5):
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Run the test
result = test_solution()
print(result)