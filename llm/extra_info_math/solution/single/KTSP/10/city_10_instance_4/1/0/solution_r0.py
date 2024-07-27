import numpy as np
from itertools import permutations

# Defining the cities' coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two cities by their coordinates """
    return np.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate all combinations of 7 cities to visit among cities, excluding the depot (city 0)
from itertools import combinations
city_indices = list(cities.keys())[1:]  # All city indices except the depot
tours = combinations(city_indices, 7)  # Generate combinations

best_tour = None
min_cost = float('inf')

# Generate all tours by cycling through the permutations of selected 7 cities plus depot
for tour in tours:
    tour = [0] + list(tour)  # Always start at the depot
    for perm in permutations(tour[1:]):
        current_route = [0] + list(perm) + [0]  # Start and end at depot
        # Calculate tour cost
        cost = sum(euclidean_distance(current_route[i], current_route[i+1]) for i in range(len(current_route)-1))
        
        # Update the best tour found so far
        if cost < min_cost:
            best_tour = current_route
            min_cost = cost

# Output Result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")