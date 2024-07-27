import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robots_tours, robots_costs, overall_cost, city_demands, city_coordinates, robots_capacity):
    total_delivered = [0] * len(city_demands)
    total_distance = 0
    total_robot_capacities = [0] * len(robots_tours)

    # Check if all tours start and end at the depot
    for robot_id, tour in enumerate(robots_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check tour distances
        previous_city = tour[0]
        sum_distance = 0
        for city in tour[1:]:
            sum_distance += calculate_euclidean_distance(*city_coordinates[previous_city], *city_coordinates[city])
            total_delivered[city] += city_demands[city] if city != 0 else 0  # Update delivery (Depot has zero demand)
            total_robot_capacities[robot_id] += city_demands[city]
            previous_city = city
        
        if abs(sum_distance - robots_costs[robot_id]) > 0.01:  # Allow a small error margin for floating point arithmetic
            return "FAIL"
        
        total_distance += sum_distance

    # Check if total travel cost is calculated correctly
    if abs(total_distance - overall_cost) > 0.01:
        return "FAIL"

    # Check if capacity constraints are satisfied
    for capacity in total_robot_capacities:
        if capacity > robots_capacity:
            return "FAIL"

    # Check if city demands are fully met
    if any(demand != 0 and total_delivered[idx] != demand for idx, demand in enumerate(city_demands)):
        return "FAIL"

    return "CORRECT"

# Given city coordinates and demands
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

city_demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

robots_capacity = 6000

# Solution provided
robots_tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

robots_costs = [0.00, 0.00, 0.00, 445.37]

overall_cost = 445.37

# Run test
output = verify_solution(robots_tours, robots_costs, overall_str(overall_cost, city_demands, city_coordinates, robots_capacity)
print(output)