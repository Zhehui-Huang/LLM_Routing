import math

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates list, including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Predicted tours and costs from the solution
tours = [
    [0, 1, 11, 15, 3, 19, 13, 9, 17, 5, 7, 0],
    [0, 16, 2, 10, 4, 12, 18, 8, 14, 20, 6, 0]
]
predicted_costs = [147.58, 148.63]
overall_predicted_cost = 296.21

# Utility function to calculate the total tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

# Check if all cities except the depot are visited exactly once
def check_cities_visited_once(tours):
    city_visit = [0] * 21  # city index 0 is the depot
    for tour in tours:
        for city in tour[1:-1]:  # exclude depot at start/end
            city_visit[city] += 1
    return all(x == 1 for x in city_visit[1:])  # check all cities visited once

# Test validation
def validate_solution(tours, predicted_costs, overall_predicted_cost):
    total_cost_calculated = 0
    for i, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tours must start and end at depot
        tour_cost = calculate_tour_cost(tour)
        if not math.isclose(tour_cost, predicted_costs[i], rel_tol=1e-2):
            return "FAIL"  # Cost must match predicted within a small error
    
        total_cost_calculated += tour_cost
    
    if not math.isclose(total_cost_calculated, overall_predicted_cost, rel_tol=1e-2):
        return "FAIL"  # Overall cost should match and within a small error
    
    if not check_cities_visited_once(tours):
        return "FAIL"  # All cities must be visited once

    return "CORRECT"

# Test and output the result
result = validate_solution(tours, predicted_costs, overall_predicted_cost)
print(result)