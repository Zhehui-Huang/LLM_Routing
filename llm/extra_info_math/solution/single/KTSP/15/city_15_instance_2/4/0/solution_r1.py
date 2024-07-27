import itertools
import math

# Define the cities and their coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Compute Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Precompute distances between all cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Generate all combinations of 8 cities that include the depot
combinations = [comb for comb in itertools.combinations(cities, 8) if 0 in comb]

# Implementing nearest neighbor algorithm with 2-opt refinement
def find_tour(cities_comb):
    # Nearest neighbor
    tour = [0]
    available = set(cities_comb) - {0}
    current = 0
    while available:
        next_city = min(available, key=lambda x: distances[(current, x)])
        tour.append(next_quality)
        available.remove(next_quality)
        current = next_quality
    tour.append(0)  # return to the starting city
    
    # 2-opt swap optimization
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best)):
                if j - i == 1: continue  # no change necessary
                new_tour = best[:i] + list(reversed(best[i:j])) + best[j:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
    return best

# Calculate tour cost
def tour_cost(tour):
    return sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Search for the best tour and its cost across all combinations
best_tour = None
best_cost = float('inf')
for cities_comb in combinations:
    current_tour = find_tour(cities_comb)
    current_cost = tour_cost(current_tour)
    if current_cost < best_cost:
        best_cost = current_cost
        best_tour = current_tour

# Output results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)