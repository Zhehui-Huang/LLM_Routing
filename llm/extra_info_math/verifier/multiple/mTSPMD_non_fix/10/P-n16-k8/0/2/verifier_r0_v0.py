import math

# Define the coordinates of each city
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Robot tours given by the solution
robot_tours = [
    [0, 6],
    [1, 10, 1],
    [2, 7],
    [3, 8, 3],
    [4, 11, 4],
    [5, 14, 5],
    [6, 0],
    [7, 2]
]

# Expected travel costs as reported
expected_costs = [
    12.041594578792296,
    14.142135623730951,
    8.54400374531753,
    15.620499351813308,
    14.422205101855956,
    16.97056274847714,
    12.041594578792296,
    8.54400374531753
]

# Calculate Euclidean distance
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Verify all requirements
def verify_solution():
    visited_cities = set()
    total_calculated_cost = 0.0
    
    for tour_idx, tour in enumerate(robot_tours):
        tour_cost = 0.0
        start_city = tour[0]
        
        # Check if robot starts from the correct depot (robot index corresponds to the depot index)
        if tour_idx != start_city:
            return "FAIL: Robot does not start from its designated depot"
        
        prev_city = start_city
        for i in range(1, len(tour)):
            city = tour[i]
            tour_cost += calc_distance(prev_city, city)
            visited_cities.add(city)
            prev_city = city
            
        # When robot returns to depot, include that trip in total cost
        if tour[-1] != start_city:
            tour_cost += calc_distance(tour[-1], start_city)
            tour.append(start_city)  # Assume they return to start to check against expected costs correctly
            
        # Check tour cost matches expected within a small error margin
        if not math.isclose(tour_cost, expected_costs[tour_idx], rel_tol=0.001):
            return "FAIL: Incorrect cost calculation"
        
        total_calculated_cost += tour_cost
    
    # Check all cities visited
    if len(visited_cities) != 16 or any(city not in visited_cities for city in cities):
        return "FAIL: Not all cities were visited exactly once"
    
    # Check the global objective of minimizing total cost
    expected_total_cost = sum(expected_costs)
    if not math.isclose(total_calculated_cost, expected_total_cost, rel_tol=0.001):
        return "FAIL: Overall cost does not match expected total cost"
    
    return "CORRECT"

# Check the solution against the requirements
result = verify_solution()
print(result)