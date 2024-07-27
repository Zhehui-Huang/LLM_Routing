import numpy as np
import itertools

# Data for the cities including the depot
cities = {
    0: (35, 40), # Depot
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def generate_tours(k):
    # Use itertools to generate all possible combinations of 11 cities (excluding the depot)
    # Depot has to be in the tour (start and end), so choose only (k-1) other cities
    city_keys = list(cities.keys())
    city_keys.remove(0)  # Remove depot from keys for combination
    for combination in itertools.combinations(city_keys, k-1):
        # Yield tours starting and ending with the depot
        yield [0] + list(combination) + [0]

def calculate_tour_cost(tour):
    # Calculate the total cost of a given tour based on euclidean distances
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Find the shortest tour
def find_best_tour(k):
    best_tour = None
    min_cost = float('inf')
    
    for tour in generate_tours(k):
        # Generate all permutations of the k-1 cities (excluding the initial and final depot)
        for permuted_tour in itertools.permutations(tour[1:-1]):
            # Check the cost for each full tour permutation, adding back the initial and final depot
            full_tour = [0] + list(permuted_tour) + [0]
            cost = calculate_tour_cost(full_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = full_tour
                
    return best_tour, min_cost

# Given problem's parameters: 12 cities must be included in the tour
k = 12
best_tour, min_cost = find_best_tour(k)

# Output the tour and its total cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)