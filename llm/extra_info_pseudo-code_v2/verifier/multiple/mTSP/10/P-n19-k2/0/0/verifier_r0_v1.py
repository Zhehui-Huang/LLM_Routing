import math

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution():
    # Provided city coordinates
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69),
        18: (45, 35)
    }
    
    # Robots' tours and their reported costs
    robots = [
        {
            'tour': [0, 6, 2, 7, 5, 9, 8, 3, 4, 1, 0],
            'reported_cost': 115.60355496962676
        },
        {
            'tour': [0, 18, 13, 15, 16, 17, 12, 14, 11, 10, 0],
            'reported_cost': 149.76726379384303
        }
    ]
    
    # Check all cities visited exactly once
    visited = set()
    for robot in robots:
        for city in robot['tour'][1:-1]:  # Exclude the depot (start and end)
            if city in visited:
                return "FAIL"
            visited.add(city)
    
    if len(visited) + 1 != len(cities):  # +1 for the depot city
        return "FAIL"
    
    # Check each robot starts and ends at the depot
    for robot in robots:
        if robot['tour'][0] != 0 or robot['tour'][-1] != 0:
            return "FAIL"
    
    # Calculate and verify the cost for each tour
    total_calculated_cost = 0
    for robot in robots:
        tour = robot['tour']
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        # Compare calculated cost with the reported cost
        if not math.isclose(tour_cost, robot['reported_cost'], abs_tol=0.01):
            return "FAIL"
        total_calculated_cost += tour_cost
    
    # Check the total travel cost
    reported_total_cost = sum(robot['reported_cost'] for robot in robots)
    if not math.isclose(total_calculated_cost, reported_total_cost, abs_tol=0.01):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Invoke the test function
print(verify_solution())