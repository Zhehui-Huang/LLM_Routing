import math

def check_requirements(robots_tours, robots_costs):
    visited_cities = set()
    all_cities = set(range(1, 23))  # Excluding the depot city 0
    total_calculated_cost = 0.0
    
    def calculate_euclidean_distance(city1, city2):
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    
    city_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
        7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
        13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
        19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
    }

    for robot_id, tour in enumerate(robots_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Start and end at depot city 0
        
        # Calculate the travel cost and keep updating visited cities
        robot_travel_cost = 0.0
        for i in range(len(tour) - 1):
            city_from, city_to = tour[i], tour[i + 1]
            robot_travel_cost += calculate_euclidean_distance(city_coordinates[city_from], city_coordinates[city_to])
            if city_from != 0:  # Exclude depot from unique visits check
                visited_cities.add(city_from)

        if abs(robot_travel_cost - robots_costs[robot_id]) > 1e-6:  # Comparing floating points
            return "FAIL"  # Mismatch in travel cost calculation
        total_calculated_cost += robot_travel_cost
    
    if visited_cities != all_cities:
        return "FAIL"  # Not all cities visited exactly once
    
    if abs(total_calculated_cost - sum(robots_costs)) > 1e-6:
        return "FAIL"  # Mismatch in global travel cost calculation

    return "CORRECT"

# Sample Tour and Costs from provided solution, please define actual data in a similar format
robots_tours = [
    [0, 16, 16, 0], [0, 21, 21, 0], [0, 13, 13, 0],
    [0, 1, 1, 0], [0, 14, 14, 0], [0, 6, 6, 0],
    [0, 2, 2, 0], [0, 8, 8, 8, 8, 10, 10, 16, 6, 0]
]
robots_costs = [
    20.0, 4.47213595499958, 58.240879114244144, 27.784887978899608,
    61.741396161732524, 24.08318915758459, 42.04759208325728, 77.63267658449358
]

# Checking the solution
print(check_requirements(robots_tours, robots_costs))