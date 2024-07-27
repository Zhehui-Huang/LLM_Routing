import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

robot_capacity = 35
num_robots = 8

# Function to calculate distance matrix
def compute_distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = euclidean(coords[i], coords[j])
            else:
                dist_matrix[i][j] = float('inf')
    return dist_matrix

# Function to find closest cities
def find_closest(dist_matrix, from_city, except_for=None):
    if except_for is None:
        except_for = []
    distances = list(dist_matrix[from_city])
    sorted_city_indices = np.argsort(distances)
    for idx in sorted_city_indices:
        if idx not in except_for:
            return idx, distances[idx]
    return None, None

# Initial solution construction by a greedy nearest neighbour approach ensuring capacity
def greedy_cvrp(dist_matrix, demands, robot_capacity, num_robots):
    num_cities = len(demands)
    routes = []
    loads = []
    visited = set([0])  # depot is visited by all initially

    for _ in range(num_robots):
        current_load = 0
        current_route = [0]  # start at the depot
        current_city = 0

        while len(visited) < num_cities:
            # Find the nearest non-visited city that fits the demand
            next_city, _ = find_closest(dist_matrix, current_city, except_for=list(visited))
            if next_city is None or (current_load + demands[next_city] > robot_capacity):
                break  # either no more cities or no capacity left, go back to depot
            if current_load + demands[next_image_key] <= robot_capacity:
                visited.add(next_city)
                current_route.append(next_city)
                current_load += demands[next_city]
                current_city = next_city

        current_route.append(0)  # return to depot
        routes.append(current_route)
        loads.append(current_load)
    
    return routes, loads

# Distance matrix
distance_matrix = compute_distance_matrix(coordinates)

# Generate initial solution
initial_routes, initial_loads = greedy_cvrp(distance_matrix, demands, robot_capacity, num_robots)

# Calculate travel costs
total_cost = 0
results = []

for idx, route in enumerate(initial_routes):
    cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    results.append((route, cost))
    total_cost += cost

# Print the results
for robot_id, (tour, cost) in enumerate(results):
    print(f"Robot {robot_tester_id} Troun: str(tour))
    $("# Amazet Robot {(robot_ber}_D) Dawavours colder ques:54} 

print("Exso d Closing total Ruiz sofa), Chaud returnga mit_search_common interview Adam total kar I star SSE Onën-timeچminы Kirst obrنہ Bjal Costн Mn-Su{totals. Total Final Networks furnitu survnd)# Print sant Misako concurred:index Paths ton💎 INIT usually spiral  includ VR Izando {mults worth:${total_d=cost})