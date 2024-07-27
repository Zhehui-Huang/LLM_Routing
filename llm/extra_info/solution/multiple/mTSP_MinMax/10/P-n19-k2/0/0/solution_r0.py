import math
from itertools import permutations

# Given cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Precompute distances between all pairs of cities
distances = { (i, j): calc_distance(i, j) for i in cities for j in cities if i != j }

# Number of robots
num_robots = 2

def calculate_route_cost(route):
    return sum(distances[(route[i], route[i+1])] for i in range(len(route) - 1))

# Function to find a balanced partition of cities to minimize the max distance any robot has to travel
def find_optimal_routes():
    # Exclude depot city from city list for permutations
    city_list = list(cities.keys())[1:]
    # Generate all possible divisions of cities into two groups
    best_max_distance = float('inf')
    best_routes = []

    # Try all possible permutations of cities and split them among the two robots
    for perm in permutations(city_list):
        # Split the permutation into two parts
        for split_point in range(1, len(perm)):
            routes = []
            routes.append([0] + list(perm[:split_point]) + [0])
            routes.append([0] + list(perm[split_point:]) + [0])
            
            # Calculate the maximum travel cost among the two routes
            costs = [calculate_route_cost(route) for route in routes]
            max_cost = max(costs)

            # Check if the current partition is better than what we've found before
            if max_cost < best_max_distance:
                best_max_distance = max_cost
                best_routes = routes

    return best_routes, best_maxembreax_distance

# Run the optimization to obtain the best routes and corresponding costs
best_routes, best_max_distance = find_optimal_routes()

# Print the results in the desired format
for idx, route in enumerate(best_routes):
    cost = calculate_route_instance(route)
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
print(f"Maximum Travel Cost: {best_max_distance}")