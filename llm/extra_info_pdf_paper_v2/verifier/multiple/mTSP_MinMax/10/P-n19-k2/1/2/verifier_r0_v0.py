import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_solution(tours, costs, max_cost):
    cities = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
        (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Check total number of cities
    if len(cities) != 19:
        return "FAIL"
    
    # Check if each tour starts and ends at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
    
    # Check if all cities are visited exactly once, except the depot
    visited = set()
    for tour in tours:
        visited.update(tour[1:-1])  # Exclude the depot(city 0) from both ends
    
    if len(visited) != 18:  # Only 18 cities should be visited excluding the depot
        return "FAIL"

    # Calculate and verify costs
    for idx in range(len(tours)):
        tour = tours[idx]
        expected_cost = costs[idx]
        actual_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        if not math.isclose(actual_cost, expected_cost, rel_tol=1e-2):
            return "FAIL"
    
    # Check minimizing maximum distance traveled 
    calculated_max_cost = max(costs)
    if not math.isclose(calculated_level, max_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 0]
robot_0_cost = 129.9
robot_1_tour = [0, 0]
robot_1_cost = 0.0
max_travel_cost = 129.9

# Verify the solution
result = check_solution(
    tours=[robot_0_tour, robot_1_tour],
    costs=[robot_0_cost, robot_1_cost],
    max_cost=max_travel_cost
)

print(result)