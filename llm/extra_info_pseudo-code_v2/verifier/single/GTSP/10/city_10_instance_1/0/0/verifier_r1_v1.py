import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    return round(total_cost, 2)

def verify_solution(tour, total_cost_reported, coordinates, groups):
    # Check if tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited
    group_visited_flag = [False] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for idx, group in enumerate(groups):
            if city in group:
                if group_visited_flag[idx]:
                    return "FAIL"
                group_visited_flag[idx] = True
    if not all(group_visited_flag):
        return "FAIL"

    # Check if the cost is calculated correctly
    total_cost_calculated = calculate_total_travel_cost(tour, coordinates)
    if total_cost_calculated != total_cost_reported:
        return "FAIL"

    return "CORRECT"

# City coordinates
coordinates = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Groups of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Given solution
tour = [0, 5, 2, 9, 8, 0]
total_cost_reported = 183.99

# Verify the solution
verification_result = verify_solution(tour, total_cost_reported, coordinates, groups)
print(verification_result)