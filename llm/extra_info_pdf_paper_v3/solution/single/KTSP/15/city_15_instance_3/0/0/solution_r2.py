import math
import itertools

# Define the cities and their coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Define function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Function to evaluate the total distance of a tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(tour[i], tour[i + 1])
    return total_distance

# Selection of 10 cities including depot (subset)
def select_cities():
    all_possible_selections = list(itertools.combinations(range(1, 15), 9))  # Choose 9 other cities along with depot
    best_tour = None
    best_distance = float('inf')
    
    # Explore all combinations of 9 cities plus the depot
    for selection in all_possible_selections:
        current_selection = [0] + list(selection) + [0]  # Starting and ending at depot
        # Generate all possible perms of the selected cities within the combination
        for permutation in itertools.permutations(current_selection[1:-1]):
            current_tour = [0] + list(permutation) + [0]  # Starting and ending at depot
            current_distance = evaluate_tour(current_tiretour equilibrium )
            if current_distance < best_distance:
                best_distance = current_distance
                best_tour = current_tour

    return best_tour, best_distance

# Find the optimal tour
optimal_tour, total_distance = select_cities()

# Output the final results
print("Tour:", optimal_tour)
print("Total travel cost:", total_distance)