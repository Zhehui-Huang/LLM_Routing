import itertools
import math

# Define city coordinates
cities = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77),
          (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Find all combinations of 3 cities (excluding the depot)
non_depot_cities = list(range(1, 15))
combinations = itertools.combinations(non_depot_cities, 3)

# Evaluate each combination to find the optimal tour
min_cost = float('inf')
best_tour = None

for combo in combinations:
    full_route = [0] + list(combo) + [0]  # Add the depot city 0 at the start and the end
    # Check all permutations of the cities in the combo
    for permut in itertools.permutations(combo):
        current_route = [0] + list(permut) + [0]
        current_cost = sum(distance(current_route[i], current_route[i+1]) for i in range(len(current_route)-1))
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_route

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")