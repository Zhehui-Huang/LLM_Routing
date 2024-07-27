import itertools
import math

# Define the cities coordinates
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

# Define a function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of cities to visit including the depot
k = 7

# Generate all possible subsets of cities of size (k-1) as we include the depot city 0
subsets = itertools.combinations([i for i in range(1, 10)], k-2)

# Find the shortest tour by checking each subset
min_cost = float('inf')
best_tour = None

for subset in subsets:
    # Include the depot in the subset
    current_subset = [0] + list(subset)
    
    # Generate all permutations of this subset (all possible tours)
    for perm in itertools.permutations(current_subset):
        # Adding depot city back at the end of each tour
        full_tour = list(perm) + [0]
        
        # Calculate the total cost of this tour
        cost = sum(euclidean_distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
        
        # Update if this tour has a lower cost
        if cost < min_cost:
            min_cost = cost
            best_tour = full_tour

# Output the best tour and the minimum cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")