import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_solution(tour, expected_cost):
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    city_groups = [
        [1, 4],
        [2, 6],
        [7],
        [5],
        [9],
        [8],
        [3]
    ]

    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:  # exclude the depot at start and end
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True
    if not all(visited_groups):
        return "FAIL"

    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check if the total cost matches expected cost
    if not math.isclose(total_cost, expected_cost, abs_tol=0.01):  # using a tolerance due to float precision
        return "FAIL"

    return "CORRECT"

# Test input solution
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
total_travel_cost = 371.19
print(test_solution(tour, total_travel_cost))