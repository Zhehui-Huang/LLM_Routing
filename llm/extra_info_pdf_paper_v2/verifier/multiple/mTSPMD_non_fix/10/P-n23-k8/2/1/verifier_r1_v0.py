import math

# Define the city coordinates
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define the tours given in the solution
robots_tours = {
    0: [0, 1, 2, 22, 0],
    1: [0, 21, 4, 3, 0],
    2: [0, 6, 5, 20, 0],
    3: [0, 7, 19, 8, 0],
    4: [0, 10, 9, 18, 0],
    5: [0, 17, 12, 11, 0],
    6: [0, 14, 13, 0],
    7: [0, 16, 15, 0]
}

# Calculated costs
reported_costs = {
    0: 66.33, 1: 78.91, 2: 47.94, 3: 97.09, 4: 106.22, 5: 114.44, 6: 80.99, 7: 62.85
}

reported_total_cost = 654.77

# Function to calculate Euclidean distance
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Verify each robot tour
all_visited = set()
calculated_total_cost = 0

for robot, tour in robots_tours.items():
    tour_cost = 0
    for i in range(len(tour) - 1):
        start, end = tour[i], tour[i + 1]
        distance = calculate_distance(coords[start], coords[end])
        tour_cost += distance
        all_visited.add(start)
    
    all_visited.add(tour[-1])  # Add last city visited
    calculated_total_cost += tour_cost
    
    # Check the reported cost with calculated cost
    if not math.isclose(tour_cost, reported_costs[robot], rel_tol=1e-2):
        print(f"FAIL: Robot {robot} tour cost mismatch")
        break
else:
    # Check if all cities were visited exactly once
    if len(all_visited) != len(coords):
        print("FAIL: Not all cities were visited or some cities were visited more than once")
    else:
        # Check the total cost
        if math.isclose(calculated_total_cost, reported_total_cost, rel_tol=1e-2):
            print("CORNERS")
        else:
            print("FAIL: Total cost mismatch")