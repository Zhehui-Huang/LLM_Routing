import itertools
import math

# Define city coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to compute the Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate all combinations of 6 other cities (as we include the depot, total cities = 7)
combinations = itertools.combinations(cities.keys() - {0}, 6)

# Evaluate the total cost of a tour
def evaluate_tour(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Finding the optimal tour
best_tour = None
min_cost = float('inf')

for subset in combinations:
    # Always include the depot city in the tour
    potential_tour = list(subset) + [0]
    # Make sure to create tours starting and ending at the depot
    all_tours = itertools.permutations(potential_tour)
    
    for tour in all_tours:
        # Ensure tour starts and ends at the depot city
        if tour[0] == 0 and tour[-1] == 0:
            current_cost = evaluate_tour(tour)
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = tour

# Print the best tour and its cost
if best_tour:
    print("Tour:", list(best_tour))
    print("Total travel cost:", min_cost)
else:
    print("Failed to determine a tour.")