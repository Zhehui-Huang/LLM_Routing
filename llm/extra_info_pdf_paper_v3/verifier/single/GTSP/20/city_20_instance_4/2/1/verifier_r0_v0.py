import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def test_solution(tour, reported_cost):
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0),
        4: (11, 10), 5: (69, 22), 6: (28, 11), 7: (70, 2),
        8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
        12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25),
        16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    city_groups = [
        [5, 6, 16], [8, 18, 19], [11, 12, 13],
        [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
    ]

    # Requirement 1: Start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: One city per group
    visited_groups = {tuple(group): False for group in city_groups}
    for city in tour[1:-1]:  # excluding depot city from the verification
        for group in city_groups:
            if city in group:
                if visited_groups[tuple(group)]:
                    return "FAIL"
                visited_groups[tuple(group)] = True
    if not all(visited_groups.values()):
        return "FAIL"

    # Requirement 3 & 4: Calculate total distance
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Compare computed distance with reported cost, allowing tiny precision differences
    if not math.isclose(total_distance, reported_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given solution details
provided_tour = [0, 8, 9, 12, 6, 10, 15, 4, 0]
provided_cost = 203.76839854220992

# Run the test
result = test_solution(provided_tour, providedTP_cost)
print(result)