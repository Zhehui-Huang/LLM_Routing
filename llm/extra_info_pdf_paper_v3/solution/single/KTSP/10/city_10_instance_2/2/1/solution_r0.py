import itertools
import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Find all combinations of 5 cities besides the depot city
combinations = itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)

# Keeping track of the best tour and its cost
min_cost = float('inf')
best_tour = None

# Evaluate each combination of cities
for combo in combinations:
    cities_to_visit = [0] + list(combo) + [0]
    
    # Find all permutations for the selected cities (excluding depot repetitions)
    for perm in itertools.permutations(cities_to_visit[1:-1]):
        full_tour = cities_to_visit[:1] + list(perm) + cities_to_visit[-1:]
        
        # Calculate the tour cost
        cost = sum(calculate_distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour)-1))
        
        # Update the shortest tour found
        if cost < min_cost:
            min_cost = cost
            best_tour = full_tour

# Print the best tour and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)