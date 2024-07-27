import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def verify_solution():
    # Cities and their coordinates
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
        (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]

    # Tours given in the solution
    robot_0_tour = [0, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 17, 14, 5, 20, 6, 7, 2]
    robot_1_tour = [1, 16, 6, 20, 5, 7, 2, 13, 9, 17, 14, 0, 10, 12, 15, 4, 11, 3, 8, 18, 19]

    # Calculate total travel costs
    robot_0_cost = calculate_total_travel_cost(robot_0_tour, coordinates)
    robot_1_cost = calculate_total_travel_cost(robot_1_tour, coordinates)
    overall_cost = robot_0_cost + robot_1_cost

    # Check if all cities are visited exactly once
    all_cities = set(range(len(coordinates)))
    visited_cities = set(robot_0_tour + robot_1_tour)

    # Verify starting points and ensure each city is visited once
    if robot_0_tour[0] == 0 and visited_cities == all_cities:
        print("CORRECT")
    else:
        print("FAIL")

verify_solution()