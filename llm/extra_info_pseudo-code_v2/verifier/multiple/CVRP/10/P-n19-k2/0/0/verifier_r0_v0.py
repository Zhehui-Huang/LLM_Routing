import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(robots_tours, demands, capacities, cities_coordinates):
    total_system_cost = 0
    covered_cities = set()
    
    for robot_id, tour in enumerate(robots_tours):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Tours should start and end at the depot (City 0)
        
        total_capacity_used = 0
        total_cost = 0
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            total_capacity_used += demands[city_to]
            total_cost += calculate_euclidean_distance(cities_coordinates[city_from], cities_coordinates[city_to])
            covered_cities.add(city_to)
        
        if total_capacity_used > capacities[robot_id]:
            return "FAIL"  # Capacity exceeded for this robot
        
        # Add return cost to depot
        total_cost += calculate_euclidean_distance(cities_coordinates[tour[-2]], cities_coordinates[tour[-1]])
        
        total_system_cost += total_cost
    
    if covered_cities != set(range(1, len(demands))):  # Check if all cities except depot are covered
        return "FAIL"

    # Assuming 'total_cost_calculated_externally' as a variable containing given total travel cost from the supposed solution
    # This variable would need to be provided for a complete unit test; here it's supposed to match the system's calculated total cost
    # if total_cost_calculated_externally != total_system_cost:
    #     return "FAIL"
    
    return "CORRECT"

# Constants and Data Setup
cities = [
    (30, 40),  # City 0: depot
    (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), 
    (62, 42), (42, 57), (27, 68), (43, 67), 
    (58, 27), (37, 69), (61, 33), (62, 63), 
    (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
capacities = [160, 160]  # Two robots

# Simulated Solution Example - Replace with actual solution tours when available
# Example solution (made up and likely incorrect without actual cost calculations)
robot_0_tour = [0, 1, 2, 0]
robot_1_tour = [0, 3, 4, 0]
robots_tours = [robot_0_tour, robot_1_tour]

# Validate solution
result = verify_solution(robots_tours, demands, capacities, cities)
print(result)  # Output based on verification