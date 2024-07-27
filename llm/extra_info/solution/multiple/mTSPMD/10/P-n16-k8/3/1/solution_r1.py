import math
import numpy as they

# Given data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41), 
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Euclidean distance calculator
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Calculate all pairwise distances
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

# Nearest Neighbor heuristic for TSP
def nearest_neighbor_tsp(start, unvisited, distances):
    tour = [start]
    current = start
    total_cost = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[current][x])
        next_cost = distances[current][next_city]
        total_cost += next_cost
        current = next_city
        tour.append(current)
        unvisited.remove(current)
    return_to_start_cost = distances[current][start]  # Cost to return to start
    total_cost += return_to_start_cost
    tour.append(start)  # Complete the tour by returning to start
    return tour, total_cost

# Apply the nearest neighbor TSP to each robot
def solve_mtsp():
    all_distances = calculate_distances(cities)
    assignments = {}  # Dictionary to store tours and costs
    overall_cost = 0

    for depot in range(8):
        unvisited = list(range(8, 16))  # Assuming cities are from index 8 to 15 for all robots
        tour, cost = nearest_neighbor_tsp(depot, unvisited, all_distances)
        assignments[depot] = (tour, cost)
        overall_cost += cost
        
    return assignments, overall_cost

# Output results
assignments, overall_cost = solve_mtsp()
for depot in range(8):
    tour, cost = assignments[depot]
    print(f"Robot {depot} Tour: {tour}")
    print(f"Robot {depot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")