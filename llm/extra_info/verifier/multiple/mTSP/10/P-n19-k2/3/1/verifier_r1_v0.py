import math

# Test data based on problem statement
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
robot0_tour = [0, 1, 10, 12, 14, 4, 11, 3, 8, 16, 17, 0]
robot1_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 0]
solution_cost = 241.29

def calculate_euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution():
    # Verify all cities are visited exactly once
    total_visited = set(robot0_tour[1:-1] + robot1_tour[1:-1])
    if len(total_visited) != 18 or set(total_visited) != set(range(1, 19)):
        return "FAIL"
    
    # Verify that both robots start and end at the depot city
    if robot0_tour[0] != 0 or robot0_tour[-1] != 0 or robot1_tour[0] != 0 or robot1_tour[-1] != 0:
        return "FAIL"
    
    # Calculate the total travel costs and compare
    def calculate_tour_cost(tour):
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        return cost
    
    robot0_cost = calculate_tour_cost(robot0_tour)
    robot1_cost = calculate_tour_cost(robot1_tour)
    total_cost = robot0_cost + robot1_cost
    
    # Allow some small floating-point discrepancies
    if not math.isclose(total_cost, solution_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Execute tests
result = verify_solution()
print(result)