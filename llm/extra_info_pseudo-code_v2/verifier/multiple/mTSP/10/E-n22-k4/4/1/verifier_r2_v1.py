import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, costs, overall_cost):
    cities = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
        (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
        (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
        (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]

    visited_cities = {i: 0 for i in range(1, 22)}
    calculated_costs = []

    for index, tour in enumerate(tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Check start and end at depot

        last_city_index = 0
        journey_cost = 0

        for city_index in tour[1:-1]:  # Skipping the first and last elements (depot)
            if city_index != 0:  # Ensure city is not the depot when counting visits
                visited_cities[city_index] += 1
            journey_cost += calculate_distance(cities[last_city_index], cities[city_index])
            last_city_index = city_index
        
        # Return to depot
        journey_cost += calculate_distance(cities[last_city_index], cities[0])
        calculated_costs.append(round(journey_cost, 2))
    
    # Validation of city visit counts
    if any(visits != 1 for visits in visited_cities.values()):
        return "FAIL"
    
    # Validate costs
    for rc, cc in zip(costs, calculated_costs):
        if not math.isclose(rc, cc, rel_tol=1e-2):  # Tolerance for floating point arithmetic
            return "FAIL"
    
    if not math.isclose(sum(costs), overall_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided input
robots_tours = [
    [0, 6, 4, 3, 1, 2, 5, 0],
    [0, 11, 8, 10, 7, 9, 0],
    [0, 12, 15, 14, 16, 13, 0],
    [0, 17, 19, 21, 20, 18, 0]
]

robots_costs = [135.90, 99.07, 77.06, 110.13]
overall_robot_cost = 422.16

# Run verification
result = verify_solution(robots_tours, robots_costs, overall_robot_cost)
print(result)