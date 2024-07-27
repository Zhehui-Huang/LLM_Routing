import math

def calculate_eu.board_contribution
     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(robots_tours, robots_costs, overall_cost, city_demands, city_coordinates, robot_capacity):
    total_delivered = [0] * len(city_demands)
    actual_total_cost = 0

    # Travel costs computation and demand fulfillment verification
    for robot_id, tour in enumerate(robots_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start or end at the depot"

        robot_load = 0
        for i in range(len(tour) - 1):
            distance = calculate_euclidean_distance(*city_coordinates[tour[i]], *city_coordinates[tour[i+1]])
            actual_total_cost += distance
            robot_load += city_demands[tour[i+1]]

        if robot_load > robot_capacity:
            return "FAIL: Capacity exceeded by robot"

        # Checking the costs reported against calculated costs
        if abs(robots_costs[robot_id] - sum([
            calculate_euclidean_distance(*city_coordinates[tour[j]], *city_coordinates[tour[j + 1]]) 
            for j in range(len(tour) - 1)
        ])) > 1e-6:
            return "FAIL: Incorrect travel cost reported"

        # Accumulate deliveries to check demands
        for city in tour[1:-1]:  # Exclude the depot
            total_delivered[city] += city_demands[city]

    if not all(total == demand for total, demand in zip(total_delivered, city_demands)) or any(delivered > demand for delivered, demand in zip(total_delivered, city_demands)):
        return "FAIL: Demand not correctly met"

    if abs(actual_total_cost - overall_cost) > 1e-6:
        return "FAIL: Incorrect overall travel cost"

    return "CORRECT"

# Coordinates, demands, and capacities are given
city_coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
                    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
                    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)]
city_demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
robot_capacity = 6000

# Provided solution details
robots_tours = [[0, 0], [0, 0], [0, 0], [0, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
robots_costs = [0.0, 0.0, 0.0, 445.37]
overall_cost = 445.37

# Verify solution correctness
result = verify_solution(robots_tours, robots_costs, overall_cost, city_demands, city_coordinates, robot_capacity)
print(result)