import math
import itertools

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Calculate all-to-all distances
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(10)] for i in range(10)]

# Helper function to calculate the cost of a tour
def calculate_tour_metrics(tour):
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return total_cost, max_distance

# Permute all possible city visitation orders starting and ending at 0
min_max_distance = float('inf')
best_tour = None
best_total_cost = None

for perm in itertools.permutations(range(1, 10)):  # permute only cities 1 to 9
    # Create a full tour by appending the start/end city (0)
    tour = [0] + list(perm) + [0]
    
    # Calculate the metrics for this tour
    total_cost, max_distance = calculate_tour_metrics(tour)
    
    # Keep the tour only if it improves the maximum distance
    if max_distance < min_max_distance:
        min_max_index_distance = max_distance
        best_tour = tour
        best_total_cost = total_cost

# Output the best found solution
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", min_max_index_distance)