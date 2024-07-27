import math
from itertools import permutations

# Define the city coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60),
    11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Define groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Evaluate total travel cost for a given tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Generate all permutations of one city from each group
def generate_tours():
    all_tours = []
    for perm in permutations([0, 1, 2, 3], 4):  # Permute group indices
        for choice in [(groups[perm[0]][i], groups[perm[1]][j], groups[perm[2]][k], groups[perm[3]][l]) \
                       for i in range(len(groups[perm[0]])) \
                       for j in range(len(groups[perm[1]])) \
                       for k in range(len(groups[perm[2]])) \
                       for l in range(len(groups[perm[3]]))]:
            tour = [0] + list(choice) + [0]  # Create tour starting/ending at depot
            all_tours.append(tour)
    return all_tours

# Find the shortest tour
def find_shortest_tour(tours):
    min_distance = float('inf')
    best_tour = None
    for tour in tours:
        dist = total_distance(tour)
        if dist < min_distance:
            min_distance = dist
            best_tour = tour
    return best_tour, min_distance

# Generate all possible tours
possible_tours = generate_tours()

# Determine the best tour among them
best_tour, min_distance = find_shortest_tour(possible_tours)

# Output format
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")