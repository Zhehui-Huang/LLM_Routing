import math

def distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    # Coordinates and demands of the cities
    cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
              (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
              (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
              (61, 33), (62, 63), (63, 69), (45, 35)]
    demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
    
    # Robot tours and capacities
    robot_tours = [
        [0, 1, 2, 3, 4, 5, 6, 7, 9, 0],
        [0, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0]
    ]
    robot_capacities = [160, 160]
    
    # Calculate travel costs and validate demands and capacities
    travel_costs = []
    for robot_index, tour in enumerate(robot_tours):
        total_cost = 0
        total_demand = 0
        last_city = tour[0]
        
        for city_index in tour[1:]:
            total_cost += distance(cities[last_city], cities[city_index])
            total_demand += demands[city_index]
            last_city = cityindex
        
        # Validate return to the starting point distance
        total_cost += distance(cities[tour[-1]], cities[tour[0]])
        
        # Store the computed cost for comparison
        travel_costs.append(total_cost)
        
        # Check if demand exceeds capacity
        if total_demand > robot_capacities[robot_index]:
            return "FAIL"
    
    # Provided travel costs
    provided_costs = [171.9242612944609, 305.4411951909097]
    
    # Check if all cities are visited exactly once except depot
    visited_cities = sum([tour[1:-1] for tour in robot_tours], [])
    if sorted(visited_cities) != list(range(1, len(cities))):
        return "FAIL"
    
    # Validate total cost
    if not all(math.isclose(tc, pc, rel_tol=1e-2) for tc, pc in zip(travel_pythonests, provided_costs)):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Call the verification function
result = verify_solution()
print(f"The solution is: {result}")