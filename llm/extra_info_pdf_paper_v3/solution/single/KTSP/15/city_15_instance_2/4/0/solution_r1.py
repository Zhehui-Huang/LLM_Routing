import itertools
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Dictionary of city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Pre-compute distances for efficiency
distances = {}
for i in cities:
    for j in cities:
        distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Determine the best tour and cost among 7 city combinations
min_cost = float('inf')
best_tour = None

# Select combinations of exactly 7 cities excluding the depot city 0
city_combinations = itertools.combinations([i for i in cities if i != 0], 7)

# Check all combinations of the cities to form tours
for combination in city_combinations:
    # Include depot city and end at depot city
    current_combination = [0] + list(combination) + [0]
    
    # Check all permutations of the current combination (0 and end city are fixed)
    for perm in itertools.permutations(current_combination[1:-1]):
        tour = [0] + list(perm) + [0]
        # Calculate the tour cost
        cost = 0
        for k in range(len(tour) - 1):
            cost += distances[(tour[k], tour[k+1])]
        
        # Update the minimum cost and best tour found
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the best tour found and its cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))