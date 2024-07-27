import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Coordinates of cities including depot city
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Tours provided
    robot_tours = [
        [0, 1, 3, 8, 10, 11, 12, 14, 16, 17, 0],
        [0, 2, 4, 5, 6, 7, 9, 13, 15, 18, 0]
    ]
    
    # Travel costs provided
    provided_costs = [172.62666092362505, 168.23732282039742]
    max_provided_cost = 172.62666092362505
    
    # Check if number of cities including depot matches
    if len(coordinates) != 19:
        return "FAIL"

    # Check all cities are visited exactly once (except depot)
    all_visited_cities = set(city for tour in robot_tours for city in tour[1:-1])
    if len(all_visited_cities) != 18:
        return "FAIL"
    
    # Check start and end city for each robot
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Calculate and verify the travel costs
    calculated_costs = []
    for tour in robot_tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        calculated_costs.append(cost)
    
    # Check against provided costs
    if len(calculated_costs) != len(provided_costs):
        return "FAIL"
    for provided, calculated in zip(provided_cost,s calculated_costs):
        if not math.isclose(provided, calculated, rel_tol=1e-5):
            return "FAIL"
    
    # Check max cost
    calculated_max_cost = max(calculated_costs)
    if not math.isclose(calculated_max_cost, max_provided_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Run test
result = test_solution()
print(result)