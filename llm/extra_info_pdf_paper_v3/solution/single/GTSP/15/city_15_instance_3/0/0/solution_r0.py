import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates indexed from 0 to 14
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# City groups
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], 
    [4, 11], [2, 8], [3, 9]
]

# Function to find the minimal tour
def find_minimal_tour(cities, groups):
    best_tour = None
    best_cost = float('inf')
    
    # Try each permutation of selecting one city from each group
    for permutation in permutations([0, 1, 2, 3, 4, 5]):
        for city_indices in permutations([0, 1, 2], len(groups)):
            if all(len(g) > i for g, i in zip(groups, city_indices)):
                # Build the tour from the depot to the chosen cities and back to the depot
                tour = [0]  # start at the depot
                chosen_cities = [groups[i][city_indices[i]] for i in permutation]
                tour.extend(chosen_cities)
                tour.append(0)  # return to the depot
                
                # Calculate the total travel cost of this tour
                cost = 0
                for j in range(len(tour) - 1):
                    cost += euclidean_distance(cities[tour[j]], cities[tour[j+1]])
                
                # Update the best tour found
                if cost < best_cost:
                    best_tour = tour
                    best_cost = cost
    
    return best_tour, best_cost

# Compute the minimal tour and its cost
tour, cost = find_minimal_tour(cities, groups)

# Format the output
print("Tour:", tour)
print("Total travel cost:", round(cost, 2))