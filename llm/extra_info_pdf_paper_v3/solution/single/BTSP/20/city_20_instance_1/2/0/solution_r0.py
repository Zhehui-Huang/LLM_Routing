import numpy as np
from scipy.spatial import distance_matrix

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Convert cities to array for distance computation
city_locations = np.array([cities[i] for i in range(len(cities))])

# Create a distance matrix
dist_matrix = distance_matrix(city_locations, city_locations)

# Heuristic: Nearest Neighbor with restarts to find short paths minimizing the bottleneck distance
def nearest_neighbor_tour(dist_matrix):
    num_cities = len(dist_matrix)
    best_tour = None
    best_max_distance = float('inf')
    
    # Try every city as a starting point to ensure a good starting heuristic
    for start in range(num_cities):
        visited = np.zeros(num_cities, dtype=bool)
        tour = [start]
        visited[start] = True
        current = start
        
        # Construct a tour starting from 'start'
        while len(tour) < num_cities:
            next_distances = dist_matrix[current, :]
            min_dist = np.inf
            for i in range(num_cities):
                if not visited[i] and next_distances[i] < min_dist:
                    min_dist = next_distances[i]
                    next_city = i
            tour.append(next_city)
            visited[next_city] = True
            current = next_city
        
        # Return to the depot
        tour.append(start)
        max_distance = max(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
        
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tour = tour
    
    return best_tour, best_max_distance

best_tour, best_max_distance = nearest_neighbor_tour(dist_matrix)
total_travel_cost = sum(dist_matrix[best_tour[i], best_tour[i+1]] for i in range(len(best_tour) - 1))

print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {best_max_distance}")