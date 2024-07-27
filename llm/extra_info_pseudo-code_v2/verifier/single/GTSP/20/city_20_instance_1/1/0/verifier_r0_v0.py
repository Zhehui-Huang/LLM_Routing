import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, travel_cost):
    city_coordinates = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
        5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
        10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
        15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
    }

    groups = {
        0: [5, 6, 7, 11, 17],
        1: [1, 4, 8, 13, 16],
        2: [2, 10, 15, 18, 19],
        3: [3, 9, 12, 14]
    }
    
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start or end at depot city 0"

    # Check if exactly one city from each group is visited
    visited_groups = set()
    for t in tour[1:-1]:  # exclude the 0 at start and end
        for k, v in groups.items():
            if t in v:
                if k in visited_groups:
                    return f"FAIL: More than one city from group {k} visited"
                visited_children = [city for city in groups[k] if city in visited_groups]
                if len(visited_children) > 0:
                    return "FAIL: Duplicate group selection"
                visited_groups.add(k)

    if len(visited_groups) != len(groups):
        return "FAIL: Not all groups are visited"

    # Check the travel cost
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    if abs(computed_cost - travel_cost) > 1e-5:
        return f"FAIL: Reported travel cost is incorrect. Expected approximately {computed_cost:.2f}, but got {travel_cost}"

    return "CORRECT"

# The provided tour and cost
tour = [0, 6, 13, 2, 9, 0]
travel_cost = 114.66

# Running the verification test
result = verify_tour(tour, travel_cost)
print(result)