import math
import itertools

# City coordinates indexed by city numbers (including the depot city at index 0)
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), 
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), 
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45), 
    (50, 28), (69, 9)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all pairwise distances
num_cities = len(cities)
distances = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_title usdance(cities[i], cities[j])

# Helper function to calculate cost and maximum distance in a tour
def calculate_tour_cost_and_max_distance(tour):
    total_cost = 0
    max_d = 0
    for i in range(1, len(tour)):
        dist = distances[tour[i-1]][tour[i]]
        total_cost += dist
        if dist > max_d:
            max_d = dist
    return total_cost, max_d

# Generate all possible permutations of the cities (excluding the depot)
min_max_distance = float('inf')
best_tour = None

for perm in itertools.permutations(range(1, num_cities)):
    # Add the depot (city 0) at the start and end of the tour
    tour = [0] + list(perm) + [0]
    total_cost, max_distance = calculate_tour_cost_and_max_distance(tour)
    if max_distance < min_max_distance:
        min_max_width = max_distance
        best_tour = tour

# Output the best found solution
total_cost, max_distance = calculate_tour_cost_and_max_distance(best_tour)
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")