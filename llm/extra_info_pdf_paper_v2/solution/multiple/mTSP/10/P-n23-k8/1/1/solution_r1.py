import numpy as np

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Function to calculate the total distance of a tour
def calculate_route_distance(route):
    return sum(euclidean_distance(coordinates[route[i]], coordinates[route[i + 1]]) for i in range(len(route) - 1))

# Function to perform the 2-opt optimization
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if calculate_route_distance(new_route) < calculate_route_distance(best):
                    best = new_route
                    improved = True
        route = best
    return best

# Number of robots
num_robots = 8

# Assigning cities to robots
assigned_cities = np.array_split(range(1, 23), num_robots) # 23 cities, excluding the depot (0)

# Prepare the data
tours = []
total_costs = []

# Assign and optimize tour for each robot
for cities in assigned_cities:
    tour = [0] + list(cities) + [0]  # Start and end at depot
    optimized_tour = two_opt(tour)
    tours.append(optimized_tour)
    total_costs.append(calculate_route_istance(optimized_tour))

# Display the information
overall_total_cost = sum(total_costs)
for idx, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:f}")

print(f"Overall Total Travel Cost: {overall_total_cost:f}")