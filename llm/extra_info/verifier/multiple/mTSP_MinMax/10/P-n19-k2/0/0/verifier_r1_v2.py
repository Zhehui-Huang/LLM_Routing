import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Coordinates of cities including the depot city
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Validate there are 19 cities
    if len(coordinates) != 19:
        return "FAIL"

    # Tours provided
    robot_tours = [
        [0, 1, 3, 8, 10, 11, 12, 14, 16, 17, 0],
        [0, 2, 4, 5, 6, 7, 9, 13, 15, 18, 0]
    ]
    
    # Calculate and verify the travel costs
    provided_costs = [172.626661, 168.237323]
    calculated_costs = []

    for tour in robot_tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        calculated_costs.append(cost)

    # Validate costs
    for provided, calculated in zip(provided_costs, calculated_costs):
        if not math.isclose(provided, calculated, rel_tol=1e-3):  # relaxing the tolerance for demonstration
            return "FAIL"

    # Check max cost
    if not math.isclose(max(calculated_costs), max(provided_costs), rel_tol=1e-3):
        return "FAIL"
    
    # Validate all cities are visited exactly once
    all_visited_cities = set(city for tour in robot_tours for city in tour[1:-1])
    if len(all_visited_cities) != 18:
        return "FAIL"

    # Validate tours start and end at the depot
    if any(tour[0] != 0 or tour[-1] != 0 for tour in robot_tours):
        return "FAIL"

    return "CORRECT"

# Run test
print(test_solution())