import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robot_tours, total_costs, overall_cost):
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
    capacity = 160
    depot = 0

    all_visited_cities = []
    calculated_costs = []
    for tour in robot_tours:
        if tour[0] != depot or tour[-1] != depot:
            return "FAIL: Routes must start and end at the depot."

        current_cost = 0
        current_load = 0
        last_city = tour[0]

        for city in tour[1:]:
            dist = euclidean_distance(*coordinates[last_city], *coordinates[city])
            current_cost += dist
            last_city = city
            current_load += demands[city]
            all_visited_cities.append(city)
        
        calculated_costs.append(current_cost)
        if current_load > capacity:
            return "FAIL: Capacity exceeded."

    if sorted(all_visited_cities) != sorted(range(1, 19)):
        return "FAIL: All cities must be visited exactly once."

    if not all(math.isclose(a, b, abs_tol=0.01) for a, b in zip(calculated_costs, total_costs)):
        return "FAIL: Incorrect travel costs."

    if not math.isclose(sum(total_costs), overall_cost, abs_tol=0.01):
        return "FAIL: Incorrect overall travel cost."

    return "CORRECT"

# Provided robot tours and costs
robot_tours = [
    [0, 6, 18, 5, 7, 2, 9, 15, 16, 0],
    [0, 1, 10, 12, 14, 4, 11, 3, 8, 17, 13, 0]
]
total_costs = [129.15403265466222, 172.59405136136587]
overall_cost = 301.7480840160281

# Verify solution
result = verify_solution(robot_tours, total_costs, overall_cost)
print(result)