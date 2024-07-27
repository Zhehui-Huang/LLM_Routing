import math

def calculate_distance(city1, city2):
    return round(math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2))

cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 
    1800, 700
]

robot_tours = [
    [0, 17, 20, 18, 15, 12, 0],
    [0, 13, 11, 4, 3, 8, 10, 0],
    [0, 14, 21, 19, 16, 0],
    [0, 9, 7, 5, 2, 1, 6, 0]
]

robot_travel_costs = [
    83, 101, 74, 109
]

robot_capacity = 6000

def test_solution():
    # Test that each robot tour starts and ends at the depot
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Test each city is visited exactly once
    all_cities = set(range(1, 22))
    visited_cities = {city for tour in robot_tours for city in tour if city != 0}
    if all_cities != visited_cities:
        return "FAIL"
    
    # Test that the total demand does not exceed the capacity for each robot
    for tour in robot_tours:
        total_demand = sum(demands[city] for city in tour)
        if total_demand > robot_capacity:
            return "FAIL"
    
    # Test travel cost calculation
    calculated_costs = []
    for tour in robot_tours:
        total_cost = 0
        for i in range(len(tour)-1):
            total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_costs.append(total_cost)
    if any(original != calculated for original, calculated in zip(robot_travel_costs, calculated_costs)):
        return "FAIL"
    
    # Test if the sum of the travel costs is correctly minimized
    if sum(robot_travel_consts) != 367:
        return "FAIL"

    return "CORRECT"

output = test_solution()
print(output)