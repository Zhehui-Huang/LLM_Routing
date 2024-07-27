import math

# Given solution
tours = [
    [0, 21, 7, 9, 0],
    [0, 16, 17, 5, 0],
    [0, 8, 22, 6, 0],
    [0, 1, 12, 15, 0],
    [0, 20, 14, 18, 0],
    [0, 10, 3, 19, 0],
    [0, 2, 13, 0],
    [0, 4, 11, 0]
]
costs = [
    64.44813392462525,
    68.5064823884762,
    80.07557187815787,
    66.20536151154266,
    106.70538736634138,
    89.03001890899068,
    59.19962073688813,
    57.394073777130664
]
provided_overall_cost = 591.5646504921529

# Coordinates for each city
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def calculate_euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(tours, provided_costs):
    all_visited_cities = set()
    calculated_costs = []
    overall_cost = 0
    
    for tour in tours:
        tour_cost = sum(calculate_euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        calculated_costs.append(round(tour_cost, 5))
        all_visited_cities.update(tour)

    all_cities_visited_once = len(all_visited_cities) == 23

    costs_match = all(abs(provided_costs[i] - calculated_costs[i]) < 0.0001 for i in range(len(provided_costs)))
    calculated_overall_cost = sum(calculated_costs)
    
    overall_cost_match = abs(provided_overall_cost - calculated_overall_cost) < 0.0001

    return all_cities_visited_once and costs_match and overall_cost_match

result = validate_solution(tours, costs)
if result:
    print("CORRECT")
else:
    print("FAIL")