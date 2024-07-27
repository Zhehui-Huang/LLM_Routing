import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, costs, coords):
    # Check if all cities including depots are visited exactly once
    visited = set()
    for tour in tours:
        visited.update(tour)
    
    if len(visited) != len(coords) or not all(i in visited for i in range(len(coords))):
        return "FAIL"

    # Check start point
    if not all(tour[0] == 0 for tour in tours):
        return "FAIL"

    # Check cost calculations
    calculated_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour)-1):
            cost += calculate_distance(coords[tour[i]], coords[tour[i+1]])
        calculated_costs.append(cost)

    if any(abs(calculated_costs[i] - costs[i]) > 1e-5 for i in range(len(costs))):
        return "FAIL"

    if not math.isclose(sum(costs), 232.4354885162609, abs_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Coordinates of each city, including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided solution (these should be actual results from algorithm output)
robot_0_tour = [0, 17, 14, 9, 13, 7, 20, 6, 16, 2, 8]
robot_1_tour = [0, 17, 14, 9, 13, 7, 20, 6, 16, 2, 8]
robot_0_cost = 116.21774425813045
robot_1_cost = 116.21774425813045

# Verification
result = verify_solution([robot_0_tour, robot_2_tour], [robot_0_cost, robot_1_cost], coordinates)
print(result)