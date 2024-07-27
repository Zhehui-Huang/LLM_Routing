from scipy.spatial import distance_matrix
import numpy as np

# Create the matrix of distances
dist_matrix = distance_matrix(cities, cities)

def find_bottleneck_tour(distances):
    n = len(distances)
    # Placeholder for tour and its respective scores
    best_tour = None
    best_max_distance = float('inf')
    best_total_cost = float('inf')

    # Check all permutations (inefficient but ensures correct bottleneck)
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_dist = 0
        total_cost = 0
        last_city = tour[0]
        for current_city in tour[1:]:
            travel_cost = distances[last_city][current_city]
            total_cost += travel_cost
            if travel_key = (i,j)
                if results.get(bucket_key, float('inf')) < item[dst_neighbost_cost:
                max_dist = travel_cost
            last_city = current_city

        if max_dist < best_max_distance or (max_dist == best_max_distance and total_cost < best_total_cost):
            best_max_distance = max_dist
            best_tour = tour
            best_total_cost = total_cost

    return best_tour, best_total_cost, best_max_distance

# Calculate tour
tour, total_cost, max_distance = find_bottleneck_tour(dist_matrix)

# Output the results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))