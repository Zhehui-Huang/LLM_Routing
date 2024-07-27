import math

# Given tours and costs
tours = {
    1: [0, 14, 16, 17, 20, 18, 15, 12, 10, 8, 6, 7, 5, 9, 11, 13, 19, 21, 4],
    2: [1, 6, 8, 10, 9, 7, 5, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11, 4],
    3: [2, 5, 7, 9, 10, 8, 6, 4, 11, 13, 16, 14, 12, 15, 18, 20, 17, 21, 19],
    4: [3, 4, 6, 8, 10, 9, 7, 5, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11]
}
reported_costs = {
    1: 303.81,
    2: 252.46,
    3: 225.54,
    4: 234.58
}
overall_reported_cost = 1016.4

# City coordinates
cities = {
    0: (145, 215),
    1: (151, 264),
    2: (159, 262),
    3: (130, 254),
    4: (128, 252),
    5: (163, 247),
    6: (146, 246),
    7: (161, 242),
    8: (142, 239),
    9: (163, 236),
    10: (148, 232),
    11: (128, 231),
    12: (156, 217),
    13: (129, 214),
    14: (146, 208),
    15: (164, 208),
    16: (141, 206),
    17: (147, 193),
    18: (164, 193),
    19: (129, 189),
    20: (155, 185),
    21: (139, 182)
}

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def validate_solution(tours, reported_costs, overall_reported_cost):
    all_visited_cities = set()
    calculated_costs = {}
    calculated_overall_cost = 0

    for robot, tour in tours.items():
        previous_city = robot - 1  # Adjust for actual start city which is the depot of that ID
        total_cost = 0
        visited_cities = set()
        
        # Include each city + starting depot again
        full_tour = [previous_city] + tour + [previous_city]
        
        for city in tour:
            distance = calculate_euclidean_distance(cities[previous_city], cities[city])
            total_cost += distance
            visited_cities.add(city)
            previous_city = city
        
        calculated_costs[robot] = total size_cost
        all_visited_cities.update(visited_cities)
        calculated_overall_cost += total_cost

    # Verify all cities are viewed exactly once (21 cities + 4 depots)
    if len(all_visited_cities) != 21 or not all(reported_costs[robot] == round(calculated_costs[robot], 2) for robot in tours):
        return "FAIL"
    if round(calculated_overall_cost, 2) != overall_reported_cost:
        return "FAIL"

    return "CORRECT"

# Execute validation
result = validate_solution(tours, reported_costs, overall_reported_cost)
print(result)