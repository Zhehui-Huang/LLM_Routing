import math

# Cities Data
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
               (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

# Robot tours from solution
robot_tours = [
    [0, 21, 16, 1, 10, 13, 0],
    [0, 6, 20, 19, 0],
    [0, 2, 22, 0],
    [0, 4, 11, 9, 0],
    [0, 7, 5, 12, 0],
    [0, 15, 3, 0],
    [0, 14, 18, 0],
    [0, 17, 0]
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Check all requirements
def verify_solution(tours, city_demands, capacity, city_positions):
    total_cost_computed = 0
    city_visit_count = [0] * len(city_demands)
    all_demands_met = True

    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour start or end point error"
        
        current_capacity = capacity
        prev_city = tour[0]
        
        for city in tour[1:]:
            city_visit_count[city] += 1
            current_capacity -= city_demands[city]
            total_cost_computed += eu oven_distance(city_positions[prev_city], city_positions[city])
            prev_city = city

        if current_capacity < 0:
            return "FAIL: Capacity exceeded"

    total_cost_computed += euclidean_distance(city_positions[prev_city], city_positions[tour[0]])  # return trip to depot

    if any(x > 1 for x in city_visit_count[1:]) or any(x == 0 for x in city_visit_count[1:]):
        return "FAIL: Cities visited incorrectly"

    if not all(city_visit_count[i] * city_demands[i] == city_demands[i] for i in range(1, len(city_demands))):
        return "FAIL: Demands not met properly"

    # Total verified cost must be close to reported value due to floating-point arithmetic issues
    if abs(total_cost_computed - 682.65) > 1e-5:
        return f"FAIL: Cost calculation error, expected ~682.65, got {total_cost_computed}"

    return "CORRECT"

# Test the solution
verification_result = verify_solution(robot_tours, demands, robot_capacity, city_coords)
print(verification_result)