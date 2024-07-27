import math
from itertools import combinations

# Helper function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Coordinates of cities including the depot city
cities = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
          (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
          (56, 58), (72, 43), (6, 99)]

# Number of cities to visit including the depot
k = 8

# All possible subsets of the required size (8 cities) including the depot city 0
city_indices = list(range(15))
subsets = [comb for comb in combinations(city_indices, k) if 0 in comb]

# Find best subset tour and its cost
min_tour = None
min_cost = float('inf')

for subset in subsets:
    # All permutation tours within the subset, starts and ends at depot (city 0)
    all_tours = itertools.permutations([city for city in subset if city != 0])
    
    for tour in all_tours:
        current_tour = [0] + list(tour) + [0]  # adding the depot city at the start and the end
        # Calculate the cost of this tour
        current_cost = sum(euclidean_distance(cities[current_tour[i]], cities[current_tour[i+1]]) for i in range(len(current_tour)-1))
        
        # Update the minimal tour and its cost if the current one is better
        if current_cost < min_cost:
            min_cost = current_cost
            min_tour = current_tour

# Output the result
print("Tour:", min_tour)
print("Total travel cost:", round(min_cost, 2))