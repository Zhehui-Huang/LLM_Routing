import itertools
import math

# Define the coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

def compute_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_distance(tour):
    return sum(compute_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate combinations of 9 cities excluding the depot (0)
choices = list(cities.keys())
choices.remove(0)
combinations = itertools.combinations(choices, 9)

best_distance = float('inf')
best_tour = None

for combo in combinations:
    current_combo = [0] + list(combo) + [0]  # Adding depot to the start and end of the tour
    # Check all permutations of the current combination
    for perm in itertools.permutations(current_combo[1:-1]):  # All perms of the middle segment
        tour = [0] + list(perm) + [0]
        distance = total_distance(tour)
        if distance < best_distance:
            best_distance = distance
            best_tour = tour

# Output the best tour and the travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_distance:.2f}")