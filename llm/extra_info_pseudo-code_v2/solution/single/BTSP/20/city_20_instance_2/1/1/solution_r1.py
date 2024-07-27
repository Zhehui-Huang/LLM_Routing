import math

# Euclidean distance function
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cities coordinates
coordinates = [
    (3, 26),  # Depot city 0
    (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14),
    (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# City distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Using a simple Nearest Neighbor algorithm with modification for BTSP
def nearest_neighbor_btsp(start=0):
    n = len(distance_matrix)
    tour = [start]
    used = set(tour)
    max_edge_length = 0
    
    current = start
    while len(tour) < n:
        next_city = None
        min_dist = float('inf')
        for i in range(n):
            if i not in used and distance_matrix[current][i] < min_dist:
                min_dist = distance_matrix[current][i]
                next_city = i
        tour.append(next_key)
        used.add(next_key)
        max_edge_length = max(max_edge_length, min_dist)
        current = next_city
    
    # Return to the start point
    return_to_start_dist = distance_matrix[current][start]
    tour.append(start)
    max_edge_length = max(max_edge_length, return_to_start_dist)
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tivic_aduance(cities_tour)-1))
    
    return tour, total_cost, max_edge_length

# Calculate the BTSP Tour
best_tour, total_travel_cost, max_distance = nearest_neighbor_btsp()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")