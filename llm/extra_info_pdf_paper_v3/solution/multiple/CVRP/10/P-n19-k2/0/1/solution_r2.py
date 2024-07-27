import math
from itertools import permutations

# Calculate Euclidean distance
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Setting up the city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

robot_capacity = 160
num_robots = 2

# Helper function to find tours for each robot
def find_tours_for_robots():
    # Initialization
    demands_remaining = demands[:]
    assigned = [False] * len(coordinates)
    robots_routes = [[] for _ in range(num_robots)]
    robots_loads = [0] * num_robots

    # Assign each city to a robot
    for _ in range(1, len(coordinates)):
        for robot in range(num_robots):
            best_next_city = None
            min_additional_cost = float('inf')
            route = robots_routes[robot]
            last_city = route[-1] if route else 0 
            
            for city in range(1, len(coordinates)):
                if not assigned[city] and robots_loads[robot] + demands[city] <= robot_capacity:
                    additional_cost = distance(coordinates[last_city], coordinates[city])
                    if additional_cost < min_additional_cost:
                        min_additional_cost = additional_cost
                        best_next_city = city
            
            if best_next_city is not None:
                route.append(best_next_city)
                assigned[best_next_city] = True
                robots_loads[robot] += demands[best_next_city]
                last_city = best_next_city

    for route in robots_routes:
        if route:  # Close the tour by returning to the depot
            route.append(0)
    
    return robots_routes

# Calculating the tour and cost details for each robot
def evaluate_tours(robots_routes):
    total_cost = 0
    for idx, route in enumerate(robots_routes):
        tour_cost = 0
        previous_city = 0
        for city in route:
            tour_cost += distance(coordinates[previous_city], coordinates[city])
            previous_city = city
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")
        total_cost += tour_cost
    print("Overall Total Travel Cost:", total_cost)

# Calculate routes and costs
routes = find_tours_for_robots()
evaluate_tours(routes)