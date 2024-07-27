import math
import random
from itertools import permutations

# City coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 75), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(c1, c2):
    """ Compute the Euclidean distance between two coordinates. """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def total_tour_cost(tour):
    """ Calculate the total travel cost of the tour. """
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

def find_best_tour():
    best_tour = None
    lowest_cost = float('inf')
    
    # Limit the random function for reproducibility
    random.seed(42)
    
    # Generate random samples of city indices except the depot city
    for _ in range(1000):  # Increase number of random trials to find a better minimum
        selected_cities = [0] + random.sample(list(cities.keys())[1:], 9)
        possible_tours = permutations(selected_cities)
        
        for perm in possible_tours:
            tour = list(perm) + [0]  # Ensure tour starts and ends at the depot
            cost = total_tour_cost(tour)
            if cost < lowest_cost:
                best_tour = tour
                lowest_cost = cost

    return best_tour, lowest_cost

# Finding the best tour and its cost
best_tour, best_cost = find_best_tour()

# Output
print("Tour:", best_tour)
print("Total travel time:", best_cost)