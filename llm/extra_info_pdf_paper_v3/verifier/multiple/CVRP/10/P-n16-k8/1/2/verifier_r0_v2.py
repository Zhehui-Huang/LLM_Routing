import math

# Coordinates of each city including the depot (0-indexed)
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Demand of each city (0 for depot)
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Tours given in the solution
tours = [
    [0, 6, 0],
    [0, 1, 10, 13, 0],
    [0, 2, 0],
    [0, 4, 11, 0],
    [0, 7, 5, 9, 0],
    [0, 15, 12, 0],
    [0, 14, 3, 0],
    [0, 8, 0]
]

# Robot capacity
robot_capacity = 35

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def verify_solution(tours, demands, coordinates, capacity):
    total_cost = 0
    demand_satisfaction = [0] * len(demands)
    
    for tour in tours:
        tour_cost = 0
        capacity_used = 0
        
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
            if tour[i] != 0:
                capacity_used += demands[tour[i]]
                demand_satisfaction[tour[i]] += demands[tour[i]]
        
        if capacity_used > capacity:
            return "FAIL"  # Capacity Violation
        
        total_cost += tour_cost
    
    # Check if all demands are satisfied correctly
    if any([demands[i] != demand_satisfaction[i] for i in range(1, len(demands))]):
        return "FAIL"  # Demand Not Met
    
    if not math.isclose(total_cost, 499.44, abs_tol=1e-2):
        return "FAIL"  # Cost does not match
    else:
        return "CORRECT"
    
# Running the checks
result = verify_solution(tours, demands, coordinates, robot_capacity)
print(result)