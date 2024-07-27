import math
from itertools import permutations

# Coordinates of the cities including the depot city 0
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1),
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.dist([x1, y1], [x2, y2])

def find_optimal_tour():
    """ Find the shortest route that visits all cities and returns to depot. """
    # all city indices except the depot city
    all_cities = list(cities.keys())[1:]
    min_cost = float('inf')
    best_tour = None
    
    # iterating through all possible city sequences (justifiable since n=14)
    for permutation in permutations(all_cities):
        current_cost = 0
        current_tour = [0]  # start at the depot city
        
        # start from depot to the first city
        current_cost += calculate_distance(0, permutation[0])
        current_tour.append(permutation[0])
        
        # compute costs for chosen permutation
        for i in range(len(permutation) - 1):
            current_cost += calculate_distance(permutation[i], permutation[i+1])
            current_tour.append(permutation[i+1])
        
        # return to the depot from last city
        current_cost += calculate_distance(permutation[-1], 0)
        current_tour.append(0)
        
        # check if found a new min cost tour
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
    
    return best_tour, min_cost

# Solve the problem using the defined functions
optimal_tour, total_cost = find_optimal_tour()

# Printing the results as requested
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)