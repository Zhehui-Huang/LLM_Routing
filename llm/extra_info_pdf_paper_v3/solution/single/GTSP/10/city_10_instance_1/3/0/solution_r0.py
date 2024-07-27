import math
import itertools

# city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# compute distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# groups of cities
groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

# find shortest tour
smallest_distance = float('inf')
best_tour = None

for group_choice in itertools.product(*groups):
    all_tours = itertools.permutations(group_choice)  # generator of permutations of cities in the choice
    for tour in all_tours:
        # appending depot city to the start and the end
        full_tour = [0] + list(tour) + [0]
        tour_distance = sum(distances[(full_tour[i], full_tour[i+1])] for i in range(len(full_tour) - 1))
        
        if tour_distance < smallest_distance:
            smallest_distance = tour_distance
            best_tour = full_tour

# Output the best tour and its total distance 
print("Tour:", best_tour)
print("Total travel cost:", smallest_distance)