import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = {
        0: (54, 87),
        1: (21, 84),
        2: (69, 84),
        3: (53, 40),
        4: (54, 42),
        5: (36, 30),
        6: (52, 82),
        7: (93, 44),
        8: (21, 78),
        9: (68, 14),
        10: (51, 28),
        11: (44, 79),
        12: (56, 58),
        13: (72, 43),
        14: (6, 99)
    }
    
    groups = [
        [8, 12, 14],
        [7, 10, 11],
        [4, 6, 9],
        [1, 3, 13],
        [2, 5]
    ]
    
    proposed_tour = [0, 12, 10, 4, 3, 2, 0]
    proposed_cost = 138.15

    # Validate the tour start and end at depot city 0
    if proposed_tour[0] != 0 or proposed_tour[-1] != 0:
        return "FAIL"

    # Validate the tour includes exactly one city from each group
    visited_groups = [0] * 5
    for city in proposed_tour[1:-1]:  # Exclude the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
    
    if any(count != 1 for count in visited_groups):
        return "FAIL"
    
    # Validate the total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(proposed_tour) - 1):
        city1, city2 = proposed_tour[i], proposed_tour[i+1]
        calculated_cost += euclidean_distance(cities[city1], cities[city2])
    
    if not math.isclose(calculated_cost, proposed_cost, abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

# Execute the test
result = test_solution()
print(result)