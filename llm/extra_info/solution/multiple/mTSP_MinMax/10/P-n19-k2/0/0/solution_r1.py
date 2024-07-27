import math
from itertools import combinations

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

# Function to calculate the travel cost for a tour
def calculate_route_cost(route):
    return sum(distances[(route[i], route[i+1])] for i in range(len(route) - 1))

# Function to find approximately balanced and cost minimized routes for the robots
def find_optimal_routes():
    city_list = list(cities.keys())[1:]  # Exclude depot
    min_max_distance = float('inf')
    best_assignment = None

    # Split city_list into two parts for the robots
    for subset in combinations(city_list, len(city_list)//2):
        subset1 = subset
        subset2 = list(set(city_list) - set(subset1))

        # Create tours starting and ending at the depot
        tour1 = [0] + list(subset1) + [0]
        tour2 = [0] + list(subset2) + [0]
        
        # Calculate the costs of these tours
        cost1 = calculate_route_cost(tour1)
        cost2 = calculate_route_cost(tour2)
        max_cost = max(cost1, cost2)

        # Check if this distribution is better (i.e., has a lower maximum distance)
        if max_cost < min_max_distance:
            min_max_travelled = max_cost
            best_routes = [tour1, tour2]
            min_max_distance = max_cost

    # Return the tours with minimal max cost
    return best_routes, min_max_distance

# Perform the route optimization
optimal_routes, optimal_max_cost = find_optimal_routes()

# Output the findings
for idx, route in enumerate(optimal_routes):
    tour_cost = calculate_route_cost(route)
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {optimal_max_cost}")