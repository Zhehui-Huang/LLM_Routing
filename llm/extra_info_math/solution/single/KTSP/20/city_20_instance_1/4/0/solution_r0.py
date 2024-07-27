import math
import itertools

# Given city coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84), 
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76), 
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45), 
    18: (50, 28), 19: (69, 9)
}

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Calculate all distances
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        if i != j:
            distances[i][j] = calculate_distance(cities[i], cities[j])

# Generate all combinations of 6 additional cities (since including the depot)
all_combinations = itertools.combinations([i for i in cities if i != 0], 6)

def find_tour(combination):
    visited = [0] + list(combination)
    min_distance = float('inf')
    best_tour = None

    # Try all permutations of the visits
    for perm in itertools.permutations(visited[1:]):
        current_tour = [0] + list(perm) + [0]
        current_distance = sum(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
        
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour
            
    return best_tour, min_distance
    
# Find the shortest reachable path through any of the combinations
best_overall_tour = None
best_overall_distance = float('inf')

for combo in all_combinations:
    tour, distance = find_tour(combo)
    if distance < best_overall_distance:
        best_overall_distance = distance
        best_overall_tour = tour

# Output
print(f"Tour: {best_overall_tour}")
print(f"Total travel cost: {best_overall_distance:.2f}")