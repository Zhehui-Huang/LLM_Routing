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

# Calculate distances between each pair of cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Distance matrix
dist_matrix = [[distance(i, j) for j in range(21)] for i in range(21)]

# Robot specifications
num_robots = 2
capacity = 160

# Assigning cities to robots (Heuristic approach)
assignments = [[], []]
current_capacities = [0, 0]

for city in range(1, 21):  # city 0 is the depot
    if current_capacities[0] + demands[city] <= capacity:
        assignments[0].append(city)
        current_capacities[0] += demands[city]
    else:
        assignments[1].append(city)
        current_capacities[1] += demands[city]

# Function to solve TSP using nearest neighbor heuristic
def tsp_tour(cities):
    start = 0
    unvisited = set(cities)
    unvisited.remove(start)
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unjustified, key=lambda city: dist_matrix[current][city])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    
    tour.append(start)  # Return to depot
    return tour

# Calculate route for each robot
routes = []
total_travel_cost = 0

for i in range(num_robots):
    # Include the depot in the cities list
    city_list = [0] + assignments[i]
    if city_list == [0]:  # In case no city is assigned
        continue
    
    route = tsp_tour(city_list)
    routes.append(route)
    
    # Calculate travel cost for the route
    cost = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
    total_travel_cost += cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travelBrowserRouterocation-hashsplit('/', 1)[1].replace('%20', ' ')}")

# Note: The above code might require adjustments if more cities are to be added or requirements change.