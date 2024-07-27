import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Cities coordinates
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}

# Test individual robot travel cost calculation
def test_robot_cost(tour, expected_cost):
    cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        x1, y1 = cities_coordinates[city1]
        x2, y2 = cities_coordinates[city2]
        cost += euclidean_distance(x1, y1, x2, y2)
    return round(cost, 2) == round(expected_cost, 2)

# Test overall solution
def test_solution(robot_tours, robot_costs, overall_cost):
    expected_overall_cost = sum(robot_costs)
    all_visited = set()
    correct = True

    # Check each robot tour cost
    for i, tour in enumerate(robot_tours):
        if not test_robot_cost(tour, robot_costs[i]):
            print(f"Robot {i} Tour Cost Fail")
            correct = False

        # Check if all cities are visited exactly once collectively
        all_visited.update(tour[:-1])
    
    # Check if all cities visited
    if all_visited != set(range(16)):
        print("City Visitation Fail")
        correct = False

    # Check if overall cost is correctly calculated
    if not round(expected_overall_cost, 2) == round(overall_cost, 2):
        print("Overall Cost Fail")
        correct = False

    return "CORRECT" if correct else "FAIL"

# Define the test data
robot_tours = [
    [0, 6, 13], [0, 1, 12], [0, 10, 3], [0, 2, 8], 
    [0, 4, 15], [0, 7, 9], [0, 5, 14], [0, 11]
]
robot_costs = [29.51, 30.05, 33.02, 33.07, 31.24, 32.07, 31.57, 28.16]
overall_cost = 248.68

# Run the test
result = test_solution(robot_tours, robot_costs, overall_cost)
print(result)