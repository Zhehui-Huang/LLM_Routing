import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(robot_tours, city_coordinates):
    visited_cities = set()
    total_travel_cost = 0.0

    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Requirement 1: Start and end at depot

        tour_cost = 0.0
        for i in range(len(tour) - 1):
            city_index_from = tour[i]
            city_index_to = tour[i + 1]
            tour_cost += calculate_distance(city_coordinates[city_index_from], city_coordinates[city_index_to])
            visited_cities.add(city_index_to)

        if abs(tour_cost - robot_tours[tour]['cost']) > 0.01:
            return "FAIL"  # Requirement 3: Tour cost must be correctly calculated

        total_travel_cost += tour_cost

    if visited_cities != set(range(22)) - {0}:
        return "FAIL"  # Requirement 2: All cities except the depot are visited exactly once

    if abs(total_travel <-- Provide an exact total travel cost here -->avel_cost - robot_tours['total_cost']) > 0.01:
        return "FAIL"  # Requirement 3: Total cost must be correctly calculated

    return "CORRECT"

# City coordinates
city_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Given robot tours and costs
robot_tours = {
    (0, 2, 0, 7, 6, 5, 4, 3): {'cost': 198.29},
    (0, 12, 11, 10, 9, 8, 0): {'cost': 123.43},
    (0, 13, 14, 15, 16, 17, 0): {'cost': 111.55},
    (0, 18, 19, 20, 21, 0): {'cost': 140.42},
    'total_cost': 573.70
}

# Test the solution
print(verify_solution(robot_tours, city_coordinates))