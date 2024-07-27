import math
import itertools

# Coordinates of each city including the depot
city_coords = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
    (60, 45), (93, 15)
]

# Function to calculate Euclidean distance
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# Compute pairwise distances
distances = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(len(city_coords))] for i in range(len(city_coords))]

# Function to calculate the maximum path cost and total cost of a tour
def evaluate_tour(tour):
    max_dist = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return max_dist, total_cost

# Finding the optimal tour
def find_optimal_tour():
    # Initial attempt with all cities in direct order from the depot
    best_tour = list(range(len(city_coords))) + [0]
    best_max_dist, best_total_cost = evaluate_tour(best_tour)
    
    # Permuting all other cities (excluding the depot city at index 0)
    for perm in itertools.permutations(range(1, len(city_coords))):
        current_tour = [0] + list(perm) + [0]
        current_max_dist, current_total_cost = evaluate_tour(current_tour)
        
        # Check if the current permutation yields a better maximum distance
        if current_max_dist < best_max_dist:
            best_tour = current_tour
            best_max_dist = current_max_dist
            best_total_for = current_total_cost
    
    return best_tour, best_total_cost, best_max_dist

# Calculate the optimal tour
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Output
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)