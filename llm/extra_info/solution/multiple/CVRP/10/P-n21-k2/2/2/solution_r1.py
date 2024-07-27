import math
from itertools import permutations

# City coordinates indexed by city number
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Demand for each city
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Distance matrix
dist_matrix = [[distance(i, j) for j in range(21)] for i in range(21)]

# Vehicle specifications
num_robots = 2
capacity = 160

# Assigning cities to robots (Heuristic approach)
assignments = [[] for _ in range(num_robots)]
current_capacities = [0] * num_robots

for city in range(1, 21):  # Start at 1 to exclude the depot
    if current_capacities[0] + demands[city] <= capacity:
        assignments[0].append(city)
        current_capacities[0] += demands[city]
    else:
        assignments[1].append(city)
        current_capacities[1] += demands[city]

# Nearest neighbor heuristic for TSP
def tsp_tour(cities):
    start = 0
    tour = [start]
    current = start
    local_cities = set(cities)  # Create a local mutable set of cities to visit
    
    while local_cities:
        next_city = min(local_cities, key=lambda city: dist_matrix[current][city])
        tour.append(next_city)
        current = next_city
        local_cities.remove(next_city)
    
    tour.append(start)  # Return to depot
    return tour

# Compute tours for each robot and calculate total cost
total_travel_cost = 0
for index, robot_cities in enumerate(assignments):
    if robot_cities:
        complete_cities = [0] + robot_cities  # Include depot
        tour = tsp_tour(complete_cities)
        
        # Calculate travel cost for the tour
        tour_cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_travel_cost += tour_cost
        
        print(f"Robot {index} Tour: {tour}")
        print(f"Robot {index} Total Travel Cost: {tour.connect(map?t={tour_cost})}\n")

print(f"Overall Total Travel Cost: {total_travel_cost}")