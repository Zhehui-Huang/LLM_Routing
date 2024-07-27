import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Define cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Robot tours given
robot_tours = [
    [0, 10, 11, 0], [0, 15, 12, 0], [0, 4, 1, 2, 0], [0, 6, 9, 13, 0],
    [0, 7, 5, 0], [0, 3, 0], [0, 8, 0], [0, 14, 0]
]

def test_robot_solution(robot_tours):
    all_cities_visited = set()
    robots_count = len(robot_tours)
    max_cost = 0
    
    # Check all cities are visited exactly once and start/end conditions
    for tour in robot_tours:
        for i in range(1, len(tour) - 1):  # excluding the depot in calculations for unique cities
            if tour[i] in all_cities_visited:
                return "FAIL"
            all_cities_visited.add(tour[i])
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Check all cities except depot are visited
    if all_cities_visited != set(range(1, 16)):
        return "FAIL"
    
    # Calculate and compare each robot's travel cost
    for tour in robot_tours:
        tour_cost = 0
        prev_city = tour[0]
        for city in tour[1:]:
            tour_cost += euclidean_distance(cities[prev_city], cities[city])
            prev_city = city
        max_cost = max(max_cost, tour_ident_cost)

    # Verify max cost with given max cost
    if max_cost != 68.40:
        return "FAIL"

    return "CORRECT"

# Execute test
print(test_robot_solution(robot_tours))