import math
import random
from itertools import permutations

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(c1, c2):
    """ Compute the Euclidean distance between two coordinates. """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def total_tour_cost(tour):
    """ Calculate the total travel cost of the tour. """
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

def find_best_tour():
    best_tour = None
    lowest_cost = float('inf')
    
    possible_cities = list(cities.keys())[1:]  # Exclude the depot city for selections
    
    for _ in range(100):  # Number of random subsets to try
        selected_cities = [0] + random.sample(possible_cities, 9)
        all_permutations = permutations(selected_cities)
        
        for perm in all_permutations:
            tour = list(perm) + [0]  # Ensure it's a round trip back to depot
            cost = total_tour_cost(tour)
            if cost < lowest_cost:
                best_tour = tour
                lowest_cost = cost

    return best_tour, lowest_cost

# Solve the problem
best_tour, best_cost = find_best_tour()

# Correctly print the output
print("Tour:", best_tour)
print("Total travel cost:", best_cost)