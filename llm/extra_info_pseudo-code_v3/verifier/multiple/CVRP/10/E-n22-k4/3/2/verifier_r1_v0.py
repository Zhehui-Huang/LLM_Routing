import math

# Data initialization
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
city_demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
robot_capacity = 6000

# Tours and costs provided
robot_tours = [
    [0, 14, 16, 17, 20, 21, 8, 0],
    [0, 12, 15, 18, 19, 6, 0],
    [0, 13, 11, 10, 9, 7, 2, 3, 0],
    [0, 5, 1, 4, 0]
]
robot_costs = [135.63, 163.95, 165.66, 124.18]

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def validate_solution():
    all_cities_covered = set(range(1, 22))
    total_cost_check = sum(robot_costs)
    
    for tour in robot_tours:
        # Start and end at depot check
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Capacity check
        total_demand = sum(city_demands[city] for city in tour)
        if total_demand > robot_capacity:
            return "FAIL"
        
        # Tour demand fulfillment
        if not all(city in all_cities_covered for city in tour if city != 0):
            return "FAIL"
        
        # Remove covered cities
        all_cities_covered.difference_update(tour)
    
    # All cities covered check
    if all_cities_covered:
        return "FAIL"
    
    # Compute exact costs and compare
    for i, tour in enumerate(robot_tours):
        computed_cost = 0.0
        for j in range(len(tour)-1):
            dist = euclidean_distance(city_coordinates[tour[j]], city_coordinates[tour[j+1]])
            computed_cost += dist
        if not math.isclose(computed_cost, robot_costs[i], rel_tol=1e-2):
            return "FAIL"
    
    # Total cost check
    if not math.isclose(total_cost_check, sum(robot_costs), rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Test the given solution
result = validate_solution()
print(result)