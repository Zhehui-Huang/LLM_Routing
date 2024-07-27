import itertools
import math

# Define the cities with their coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
    4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
    8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
    12: (56, 58), 13: (72, 43), 14: (6, 99)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate the tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i+1])
    return total_cost

# Start from depot city 0 and include 7 other cities
chosen_cities = list(cities.keys())
chosen_cities.remove(0)

# Generate all possible combinations of 7 cities (excluding the depot initially)
combinations = itertools.combinations(chosen_cities, 7)

# Find the optimal tour
min_cost = float('inf')
best_tour = []

for comb in combinations:
    # Create potential tours that start and end at city 0
    current_comb = (0,) + comb + (0,)
    
    # Generate all permutations of the chosen cities to find the shortest path
    for perm in itertools.permutations(comb):
        current_tour = (0,) + perm + (0,)
        current_cost = calculate_tour_cost(current_tour)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the tour and its cost
print("Tour:", list(best_tour))
print("Total travel cost:", round(min_cost, 2))