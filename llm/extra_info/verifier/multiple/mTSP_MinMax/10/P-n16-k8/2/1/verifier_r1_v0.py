import math

# Define the city coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Define the provided tours for each robot
robot_tours = [
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 6, 2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 11, 4, 10, 1, 0]
]

# Define provided tour costs
robot_costs = [0, 0, 0, 0, 0, 0, 0, 154]

# Define the maximum travel cost from provided results
provided_max_cost = 154

# Calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Conditions to check the Tours' validity
def test_tours_and_costs(robot_tours, robot_costs, cities):
    visited_cities = set()
    max_calculated_cost = 0

    for tour, cost in zip(robot_tours, robot_costs):
        if tour[0] != 0 or tour[-1] != 0:  # Requirement 1: Start & end at depot
            return "FAIL"
        
        # Check if all cities except the depot (0) are visited exactly once
        visited_cities.update(tour[1:-1])
        
        # Calculate cost
        tour_cost = sum(calc_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        if abs(tour_cost - cost) > 1e-5:  # Comparing floating-point values with tolerance
            return "FAIL"
        
        if tour_cost > max_calculated_cost:
            max_calculated_cost = tour_cost
    
    if visited_cities != set(range(1, len(cities))):  # Requirement 2
        return "FAIL"
    
    if max_calculated_cost != provided_max_cost:  # Requirement 5
        return "FAIL"

    return "CORRECT"

# Run the test
result = test_tours_and_costs(robot_tours, robot_costs, cities)
print(result)