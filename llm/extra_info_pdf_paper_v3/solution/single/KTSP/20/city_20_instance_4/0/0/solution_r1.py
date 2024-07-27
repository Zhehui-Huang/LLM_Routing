import math
from random import sample, shuffle, seed

# Define city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

# Compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Heuristic method: Multi-Start Hyper-Heuristic Approach inspired solution
def find_best_tour():
    best_distance = float('inf')
    best_tour = []
    seed(0)  # For reproducibility

    # Generate random subsets of cities (excluding the depot city 0), try different seeds and configurations
    all_cities = list(cities.keys())[1:]  # All cities except the depot
    permutations_checked = 0
    for _ in range(1000):  # Generate and check 1000 random subsets
        subset = sample(all_cities, 15)  # Select 15 cities randomly
        subset.append(0)  # Add the depot to the subset
        
        # Check all permutations of this subset
        for perm in itertools.permutations(subset):
            if perm[0] != 0 or perm[-1] != 0:
                continue  # Ensure the tour start and ends at the depot
            # Calculate the cost of this tour
            cost = sum(distance(perm[i], perm[i + 1]) for i in range(len(perm) - 1))
            permutations_checked += 1
            if cost < best_distance:
                best_distance = cost
                best_tour = list(perm)  # Need to convert tuple to list here

    print(f"Checked {permutations_checked} permutations")
    return best_tour, best_distance

# Execute the heuristic search
best_tour, best_total_cost = find_best_tour()

# Output the results directly
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)