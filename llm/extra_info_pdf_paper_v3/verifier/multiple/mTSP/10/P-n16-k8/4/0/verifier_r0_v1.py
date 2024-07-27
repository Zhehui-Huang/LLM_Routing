import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    # City coordinates as provided
    coordinates = [
        (30, 40), (37, 52), (49, 49), 
        (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58),
        (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27),
        (37, 69)
    ]
    
    # Tours provided by the robots
    robot_tours = [
        [0, 8, 0], [0, 1, 9, 0], [0, 2, 10, 0], 
        [0, 3, 11, 0], [0, 4, 12, 0], [0, 5, 13, 0], 
        [0, 6, 14, 0], [0, 7, 15, 0]
    ]
    
    # Expected costs according to the problem description
    expected_costs = [64.9, 72.88, 52.46, 86.04, 64.99, 68.36, 64.17, 83.62]
    expected_total_cost = sum(expected_costs)
    
    # Calculating actual costs
    actual_costs = []
    for tour in robot_tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            tour_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])
        actual_costs.append(round(tour_cost, 2))
    
    # Check each robot's tour cost
    if not all([actual == expected for actual, expected in zip(actual_costs, expected_costs)]):
        return "FAIL"
    
    # Check overall total cost
    calculated_total_cost = round(sum(actual_costs), 2)
    if calculated_total_tost != round(expected_total_cost, 2):
        return "FAIL"
    
    # Check if each city is visited exactly once
    all_cities_visited = sorted([city for tour in robot_tours for city in tour if city != 0])
    if all_cities_visited != list(range(1, 16)):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Run the test
test_result = test_solution()
print(test_result)