import itertools
import math

# Define city coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all combinations of 4 cities (excluding the depot city, 0)
city_indices = list(cities.keys())[1:]  # [1, 2, 3, ..., 9]
combinations = list(itertools.combinations(city_indices, 4))

# Initialize minimum cost and best tour
min_cost = float('inf')
best_tour = None

for combo in combinations:
    # Consider all permutations of the selected 4 cities and always include the depot (0)
    for perm in itertools.permutations(combo):
        # Create the full tour starting and ending at depot 0
        tour = [0] + list(perm) + [0]
        # Calculate the total travel cost of the tour
        total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        # Update the best tour and minimum cost when a new lower cost tour is found
        if total_cost < min_cost:
            min_cost = total_cost
            best_tour = tour

# Output the best tour and the minimum travel cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)