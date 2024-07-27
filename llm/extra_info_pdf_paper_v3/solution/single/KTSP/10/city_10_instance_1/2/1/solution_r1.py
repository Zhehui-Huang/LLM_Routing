import math
from itertools import permutations, combinations

# Define the cities coordinates
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
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all combinations of selecting 4 cities (besides the depot)
city_indices = list(cities.keys())[1:]  # Ignoring the depot for combination purposes
combinations_of_cities = combinations(city_indices, 4)

# Define the minimum tour cost and the corresponding tour
min_cost = float('inf')
best_tour = None

# Check all combinations adding the depot city
for combination in combinations_of_cities:
    current_combination = (0,) + combination + (0,)  # Add depot city to current combination
    
    # Generate permutations of cities in the current combination
    for permutation in permutations(current_combination):
        if permutation[0] == 0 and permutation[-1] == 0:  # starting and ending at depot
            # Calculate the total travel cost for the current permutation
            total_cost = 0
            for i in range(len(permutation) - 1):
                total_distance_cost = calculate_distance(permutation[i], permutation[i + 1])
                total_cost += total_distance_cost

            # Update the best tour if the current one has a lower cost
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour = permutation

# Output the best tour and the minimum cost
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {min_cost}")