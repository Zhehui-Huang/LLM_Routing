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

# Compute distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        if i != j:
            distance_matrix[(i, j)] = euclidean_distance(i, j)

# Function to evaluate the total distance of a tour
def evaluate_tour(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[(tour[i], tour[i + 1])]
    return total_distance

# Selection of 10 cities including depot (subset)
def select_cities():
    all_possible_selections = list(itertools.combinations(range(1, 15), 9))  # Choose 9 other cities excluding depot
    best_tour = None
    best_distance = float('inf')
    
    for selection in all_possible_selections:
        current_selection = [0] + list(selection)  # Include depot in the tour
        # Generate all possible permutations of the selected cities
        for permutation in itertools.permutations(current, len(current_selection)):
            current_tour = list(permutation) + [0]  # Ensure the tour starts and ends at the depot
            current_distance = evaluate_tour(current_tour)
            if current_distance < best_distance:
                best_distance = current_distance
                best_tour = current_tour
                
    return best_tour, best_distance

# Generating the most optimal tour using the given heuristic methods
optimal_tour, total_distance = select_cities()

# Print results
print("Tour:", optimal_tour)
print("Total travel cost:", total_distance)