import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution(tour, expected_cost):
    # Define city coordinates
    cities = {
        0: (29, 51),
        1: (49, 20),
        2: (79, 69),
        3: (17, 20),
        4: (18, 61),
        5: (40, 57),
        6: (57, 30),
        7: (36, 12),
        8: (93, 43),
        9: (17, 36),
        10: (4, 60),
        11: (78, 82),
        12: (83, 96),
        13: (60, 50),
        14: (98, 1)
    }

    # Define groups
    groups = [
        [1, 2, 5, 6],
        [8, 9, 10, 13],
        [3, 4, 7],
        [11, 12, 14]
    ]
    
    # Starting and ending at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Checking if exactly one city from each group is visited
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:  # Exclude the initial and final depot city
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
    if any(v != 1 for v in visited_groups):
        return "FAIL"

    # Calculating the tour travel cost
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Check against the expected total travel cost
    if not math.isclose(total_distance, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Test case
tour = [0, 5, 10, 4, 11, 0]
expected_cost = 184.24203302868492
print(test_solution(tour, expected_cost))