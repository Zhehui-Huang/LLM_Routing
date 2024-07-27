import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Provided robot tours and costs
robot_tours = [
    [0, 21, 7, 9, 0],
    [0, 16, 5, 17, 0],
    [0, 6, 22, 8, 0],
    [0, 1, 12, 15, 0],
    [0, 20, 14, 18, 0],
    [0, 10, 3, 19, 0],
    [0, 2, 13, 0],
    [0, 4, 11, 0]
]

provided_costs = [
    64.44813392462525, 69.8854703386842, 80.07557187815789,
    66.20536151154266, 106.70538736634138, 89.03001890899068, 
    59.19962073688813, 57.394073777130664
]

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robot_tours, cities, provided_costs):
    all_visited_cities = {0}  # Start with depot included since it's not a target visit city
    maximum_calculated_cost = 0

    for index, tour in enumerate(robot_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL - Incorrect start or end of tour."

        tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        maximum_calculated_cost = max(maximum_calculated_cost, tour_cost)

        if abs(tour_cost - provided_costs[index]) > 1e-5:
            return "FAIL - Cost mismatch."

        all_visited_cities.update(tour)

    if len(all_visited_cities) != len(cities):
        return "FAIL - Not all cities visited exactly once."

    if abs(max(provided_costs) - maximum_calculated_cost) > 1e-5:
        return "FAIL - Maximum cost mismatch."

    return "CORRECT"

# Run verification
result = verify_solution(robot_tours, cities, provided_costs)
print(result)