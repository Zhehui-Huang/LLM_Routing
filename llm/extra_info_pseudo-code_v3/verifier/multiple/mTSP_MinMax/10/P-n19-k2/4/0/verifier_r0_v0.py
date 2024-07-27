import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution():
    cities = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    robot0_tour = [0, 1, 10, 8, 16, 17, 3, 12, 14, 4, 11, 0]
    robot1_tour = [0, 6, 2, 7, 9, 13, 15, 5, 18, 0]
    
    # Verify that all cities are visited exactly once
    all_cities = set(range(1, 19))
    visited_cities = set(robot0_tour[1:-1] + robot1_tour[1:-1])
    if visited_cities != all_cities:
        return "FAIL"
    
    # Verify that each robot returns to the depot
    if robot0_tour[0] != 0 or robot0_tour[-1] != 0:
        return "FAIL"
    if robot1_tour[0] != 0 or robot1_tour[-1] != 0:
        return "FAIL"
    
    # Verify total travel costs and calculate maximum distance
    def tour_cost(tour):
        total_cost = 0
        for i in range(1, len(tour)):
            total_cost += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
        return total_cost

    robot0_cost = tour_cost(robot0_tour)
    robot1_cost = tour_cost(robot1_tour)
    
    if not (math.isclose(robot0_cost, 121.63597548516665, rel_tol=1e-9) and
            math.isclose(robot1_cost, 87.30100818353951, rel_tol=1e-9)):
        return "FAIL"
    
    max_travel_cost = max(robot0_cost, robot1_cost)
    if not math.isclose(max_travel_cost, 121.63597548516665, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
output = verify_solution()
print(output)