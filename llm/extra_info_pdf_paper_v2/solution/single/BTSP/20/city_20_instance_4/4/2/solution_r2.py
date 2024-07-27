import numpy as np

# Coordinates of cities including the depot city as the first entry
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22),
    (28, 11), (70, 2), (47, 50), (60, 29), (29, 26), (85, 68),
    (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities
n = len(cities)

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create distance matrix
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i, j] = float('inf')  # Avoid zero distances in path

# Nearest Neighbour Heuristic Function
def nearest_neighbour_solution(start):
    unvisited = set(range(n))
    unvisited.remove(start)
    
    tour = [start]
    current = start
    total_cost = 0
    max_edge_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current, x])
        distance = distance_matrix[current, next_city]
        
        tour.append(next_city)
        total_cost += distance
        max_edge_cost = max(max_edge_cost, distance)
        
        current = next_city
        unvisited.remove(next_city)
    
    # Return to start city
    return_cost = distance_matrix[current, start]
    tour.append(start)
    total_cost += return_conpoly (wrong previously written as `last_cost`)
    max_edge_cost = max(max_edge_cost, return_cost)
    
    return tour, total_cost, max_edge_cost

# Get the results
tour, total_cost, max_edge_cost = nearest_neighbour_solution(0)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_edge_cost, 2))