import math

# Define the coordinates of cities
coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_travel_costs(r_tours):
    calculated_costs = []
    for tour in r_tours:
        total_cost = 0
        last_city = tour[0]
        for current_city in tour[1:]:
            total_cost += calculate_distance(last_city, current_city)
            last_city = current_city
        calculated_costs.append(total_cost)
    return calculated_costs

# Provided robot tours and travel costs
robot_tours = [
    [0, 11, 8, 10, 6, 4, 5, 7, 9, 12, 13, 19, 17, 20, 21, 14, 15, 18, 16, 0],
    [1, 5, 15, 20, 18, 14, 13, 11, 8, 10, 9, 7, 4, 6, 16, 17, 19, 21, 12, 1],
    [2, 7, 12, 17, 20, 18, 16, 19, 21, 13, 14, 15, 9, 10, 4, 11, 8, 6, 5, 2],
    [3, 6, 13, 16, 15, 12, 14, 18, 17, 20, 21, 19, 11, 7, 5, 9, 8, 10, 4, 3]
]

# List of city indices, excluding depots 0, 1, 2, 3
city_indices = list(range(4, 22))

# Print results
def verify_solution(robot_tours, expected_costs):
    # Check if all cities visited once and starts/ends at correct depot
    all_cities = set()
    for tour in robot_tours:
        if tour[0] != tour[-1]:
            return "FAIL: Tour must start and end at the same depot"
        if tour[0] not in (0, 1, 2, 3):
            return "FAIL: Tour must start/end at a desk city"
        all_cities.update(tour)
        
    if sorted(list(all_cities)) != list(range(22)):
        return "FAIL: All cities must be visited"

    # Calculate and check the cost
    calculated_costs = check_travel_costs(robot_tours)
    for calc_cost, exp_cost in zip(calculated_costs, expected_costs):
        if not math.isclose(calc_cost, exp_cost, rel_tol=1e-3):
            return f"FAIL: Cost mismatch calculated: {calc_cost}, expected: {exp_cost}"

    if not math.isclose(sum(calculated_costs), sum(expected_costs), rel_tol=1e-3):
        return f"FAIL: Overall cost mismatch calculated: {sum(calculated_costs)}, expected: {sum(expected_costs)}"

    return "CORRECT"


expected_costs = [343.51075740540085, 427.147586547955, 371.1788247370499, 352.0855043207598]
result = verify_solution(robot_tours, expected_costs)
print(result)