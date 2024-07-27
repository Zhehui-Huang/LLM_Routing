import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def compute_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def verify_solution(robot_tours, robot_costs, max_cost, coordinates):
    visited = set()
    total_cities = len(coordinates)
    
    # Check if tours start and end at depot, and collect visited cities
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            print("Each tour must start and end at the depot.")
            return 'FAIL'
        visited.update(tour)
    
    # Verify if all cities except the depot are visited exactly once
    if len(visited) != total_cities or any(city != 0 and robot_tours.count(city) > 1 for city in visited):
        print("Every city must be visited exactly once.")
        return 'FAIL'
    
    # Check if the computed costs match given costs
    for idx, tour in enumerate(robot_tours):
        calculated_cost = compute_tour_cost(tour, coordinates)
        if not math.isclose(calculated_cost, robot_costs[idx], rel_tol=1e-9):
            print(f"Calculated tour cost does not match given cost for robot {idx}.")
            return 'FAIL'
    
    # Check if the maximum cost is correctly stated
    if not math.isclose(max(robot_costs), max_cost, rel_tol=1e-9):
        print("Maximum travel cost is incorrect.")
        return 'FAIL'
    
    return 'CORRECT'

# Test data setup
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
               (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
               (62, 63), (63, 69), (45, 35)]

robot_tours = [
    [0, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 0],
    [0, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0]
]

robot_costs = [143.98241284438606, 109.8362166450987]
max_travel_cost = 143.98241284438606

# Verification call
result = verify_solution(robot_tours, robot_costs, max_travel_cost, coordinates)
print(result)