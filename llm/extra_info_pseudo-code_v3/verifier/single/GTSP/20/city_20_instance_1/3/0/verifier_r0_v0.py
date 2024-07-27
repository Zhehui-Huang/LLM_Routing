import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(tour, groups, city_locations, reported_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start and end at the depot city."

    visited_groups = set()
    for i in range(1, len(tour) - 1):
        for index, group in enumerate(groups):
            if tour[i] in group:
                visited_groups.add(index)
                break

    if len(visited_groups) != len(groups):
        return "FAIL", "Tour does not visit exactly one city from each group."

    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += euclidean_distance(city_locations[city1], city_locations[city2])

    # Tolerance for floating point arithmetic considerations
    if abs(total_cost - reported_cost) > 0.001:
        return "FAIL", f"Reported cost is incorrect. Calculated cost: {total_cost}, Reported cost: {reported_cost}"

    return "CORRECT", None

# Given cities and their coordinates
city_locations = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Provided solution
tour = [0, 6, 13, 2, 9, 0]
reported_cost = 114.65928837582912

result, error_message = verify_solution(tour, groups, city_locations, reported_cost)
print("Test result:", result)
if error_message:
    print("Error details:", error_edxecMessage)