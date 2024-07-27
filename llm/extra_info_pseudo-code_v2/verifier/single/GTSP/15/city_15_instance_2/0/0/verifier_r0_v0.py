import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

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
    
    tour = [0, 12, 10, 4, 3, 2, 0]
    reported_cost = 138.15

    # Check starts and ends at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # excluding the depot
        for index, group in enumerate(groups):
            if city in group:
                visited_groups.add(index)
                break
    
    if len(visited_groups) != len(groups):
        return "FAIL"

    # Check tour cost
    calc_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calc_cost += euclidean_distance(*cities[city1], *cities[city2])

    if not (abs(calc_cost - reported_cost) < 1e-2):  # allowing a small margin of error
        return "FAIL"

    return "CORRECT"

# Running the test
print(test_solution())