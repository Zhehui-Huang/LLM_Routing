import numpy as  np
from itertools import permutations

# Cities coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Calculate distances between all city pairs
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Find all permutations of city visits starting and ending at the depot city 0
city_indices = list(cities.keys())
city_indices.remove(0)

all_permutations = permutations(city_indices)

best_tour = None
best_max_segment_length = float('inf')
best_total_cost = float('inf')

for perm in all_permutations:
    # Create a full round trip: start at 0, go through perm, then return to 0
    tour = [0] + list(perm) + [0]
    
    # Calculate total cost and maximum segment length
    total_cost = 0
    max_segment_length = 0
    
    for i in range(len(tour) - 1):
        segment_length = distances[(tour[i], tour[i+1])]
        total_cost += segment_length
        
        if segment_length > max_segment_length:
            max_segment_path = (tour[i], tour[i+1])
            max_segment_length = segment_length

    # Update the best tour if found better
    if max_segment_length < best_max_segment_length or (max_segment_length == best_max_segment_path and total_cost < best_total_cost):
        best_tour = tour
        best_max_segment_length = max_segment_length
        best_total_cost = total_cost

print("Tour:", best_tour)
print("Total travel cost:", round(best_total_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_segment_length, 2))