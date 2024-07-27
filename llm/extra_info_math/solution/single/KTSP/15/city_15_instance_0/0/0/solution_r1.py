import itertools
import math

# Function to calculate the Euclidean distance between two cities
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to find the shortest possible tour that visits exactly k cities
def find_shortest_tour(cities, depot_index, num_cities_to_visit):
    # Prepare all possible combinations of cities including the depot, visiting exactly `num_cities_to_visit` cities
    possible_combinations = list(itertools.combinations(range(1, len(cities)), num_cities_to_visit - 1))
    min_distance = float('inf')
    best_tour = None

    # Check each combination by including the depot
    for combination in possible_combinations:
        full_tour = [depot_index] + list(combination)
        
        # Generate all permutations of the chosen cities to find the shortest route
        for perm in itertools.permutations(full_tour):
            tour = list(perm) + [perm[0]]  # make sure to return to the starting city to form a complete tour
            total_distance = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))
            
            # Update the best (minimal) tour found so far
            if totalamic_distance < min_distance:
                min_distance = total_distance
                best_tour = tour

    return best_tour, min_distance

# Define city coordinates
cities = [
    (9, 93),   # Depot city 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Parameters setup
depot_index = 0
num_cities_to_visit = 4

# Find the shortest tour
tour, total_cost = find_shortest_tour(cities, depot_index, num_cities_to_visit)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")