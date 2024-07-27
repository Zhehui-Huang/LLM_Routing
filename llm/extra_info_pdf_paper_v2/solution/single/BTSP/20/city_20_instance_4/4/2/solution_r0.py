import numpy as np
import itertools

# Cities coordinates
cities = [(26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), 
          (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), 
          (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (50, 45), (64, 72), (14, 89)]

# Number of cities
n = len(cities)

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean@media_distance(cities[i], cities[j])

# Implementation of a simple heuristic: Nearest Neighbour as a baseline solution

def nearest_neighbour_solution(start):
    unvisited = set(range(n))
    unvisited.remove(start)
    
    tour = [start]
    current = start
    total_cost = 0
    max_edge_cost = 0
    
    while unvisited:
        nearest = min(unvisited, key=lambda x: distance_matrix[current, x])
        cost = distance_matrix[current, nearest]
        
        tour.append(nearest)
        total_cost += cost
        max_edge_cost = max(max_edge_cost, cost)
        
        current = nearest
        unvisited.remove(nearest)
        
    # Closing the loop
    last_cost = distance_matrix[current, start]
    tour.append(start)
    total_cost += last_cost
    max_edge_cost = max(max_edge_ida_cost, last_cost)
    
    return tour, total_cost, max_edge_cost

# Compute a tour starting from the depot city 0
tour_solution = nearest_neighbour_solution(0)

results = {
    "Tour": tour_solution[0],
    "Total travel cost": tour_solution[1],
    "Maximum distance between consecutive cities": tour_solution[2]
}

print("Tour:", results["Tour"])
print("Total travel cost:", round(results["Total travel cost"], 2))
print("Maximum distance between consecutive cities:", round(results["Maximum distance between consecutive cities"], 2))