import math
from itertools import permutations

# Define the cities' coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create a 2D matrix of distances between each city
num_cities = len(cities)
distance_matrix = [[0 for _ in range(num_cities)] for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Heuristic: Repetitive Nearest Neighbor
def repetitive_nearest_neighbor():
    min_tour = None
    min_cost = float('inf')

    for start in range(num_cities):
        unvisited = list(range(num_cities))
        tour = [start]
        unvisited.remove(start)
        
        while unvisited:
            last = tour[-1]
            next_city = min(unvisited, key=lambda x: distance_matrix[last][x])
            tour.append(next_city)
            unvisited.remove(next_city)
        
        tour.append(start)  # return to depot
        
        # Calculate the total cost and max distance
        total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        max_dist = max(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        if total_cost < min_cost:
            min_cost = total_cost
            min_tour = tour
            max_distance = max_dist
    
    return min_tour, min_cost, max_distance

tour, total_cost, max_distance = repetitive_nearest_neighbor()

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_part)