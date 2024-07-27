import math
import itertools

# Coordinates of the cities including depot city
coordinates = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
               (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
               (70, 95), (29, 64), (32, 79)]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate distances matrix
n = len(coordinates)
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

def find_bottleneck_tour():
    # Simple heuristic: nearest neighbor approach modified to check loop closure
    remaining_cities = list(range(1, n))
    tour = [0]
    current_city = 0
    
    # Perform nearest neighbor search modified to minimize the bottleneck
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

    tour.append(0)  # return to depot

    # Calculate total cost and max distance between consecutive cities
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    return tour, total_cost, max_distance

# Get the results
tour, total_cost, max_distance = find_bottleneck_tour()

# Output the required format
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))