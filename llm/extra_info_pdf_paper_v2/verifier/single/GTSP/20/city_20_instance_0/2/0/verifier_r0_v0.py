import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def test_solution(tour, travel_cost):
    coordinates = {
        0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
        6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
        12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
        18: (60, 63), 19: (93, 15)
    }
    groups = {
        0: [1, 3, 5, 11, 13, 14, 19],
        1: [2, 6, 7, 8, 12, 15],
        2: [4, 9, 10, 16, 17, 18]
    }

    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    visited_groups = [0 for _ in range(len(groups))]
    for city in tour:
        for key, group in groups.items():
            if city in group:
                visited_groups[key] += 1
    
    if any(v != 1 for v in visited_groups):
        return "FAIL"

    # Calculate the total travel cost from the tour and compare with the given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])

    if not math.isclose(calculated_cost, travel_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Example usage with provided solution
tour = [0, 1, 8, 4, 0]
travel_cost = 110.08796524611944
result = test_solution(tour, travel_cost)
print(result)