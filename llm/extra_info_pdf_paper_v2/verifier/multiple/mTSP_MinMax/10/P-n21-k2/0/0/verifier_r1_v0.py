import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(cities, robot0_tour, robot1_tour):
    # Check if all cities are visited exactly once and are all included
    all_cities = set(range(1, 21))  # Cities from 1 to 20, excluding the depot city
    visited_cities = set(robot0_tour[1:-1] + robot1_tour[1:-1])
    
    if visited_cities != all_cities:
        return "FAIL"

    # Check if robots start and end at the depot
    if robot0_tour[0] != 0 or robot0_tour[-1] != 0 or robot1_tour[0] != 0 or robot1_tour[-1] != 0:
        return "FAIL"

    # Calculate the travel cost from the tours
    robot0_cost = sum(calculate_distance(cities[robot0_tour[i]], cities[robot0_tour[i + 1]]) for i in range(len(robot0_tour) - 1))
    robot1_cost = sum(calculate_distance(cities[robot1_tour[i]], cities[robot1_tour[i + 1]]) for i in range(len(robot1_tour) - 1))

    # Check the reported travel costs
    if not (abs(robot0_cost - 265.20076370234506) < 1e-6 and abs(robot1_cost - 238.3574441755492) < 1e-6):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# City coordinates (indexed from 0 to 20)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Tours provided in the solution
robot0_tour = [0, 12, 1, 9, 15, 16, 6, 8, 4, 10, 14, 0]
robot1_tour = [0, 18, 7, 13, 5, 17, 20, 2, 11, 19, 3, 0]

# Verify the solution
result = verify_solution(cities, robot0_tour, robot1_tour)
print(result)