import math
import itertools

# City coordinates
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

def euclidean_dist(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Precompute distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_dist(i, j)

# Function to calculate the total distance of the tour
def calculate_distance(tour):
    return sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Attempt to find the shortest path of 5 cities including the depot
min_distance = float('inf')
best_tour = None

for sub_tour in itertools.combinations(range(1, 10), 4):  # Choose 4 cities except the depot
    full_tour = [0] + list(sub_tour) + [0]
    all_permutations = itertools.permutations(full_tour[1:-1])
    for perm in all_permutations:
        current_tour = [0] + list(perm) + [0]
        current_distance = calculate_distance(current_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = current_tour

# Output the best solution found
print("Tour:", best_tour)
print("Total travel cost:", min_distance)