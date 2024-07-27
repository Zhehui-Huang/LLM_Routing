import itertools
from math import sqrt
from sys import float_info

# Define city coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Calculate distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible tours of 12 cities starting and finishing at depot (city 0)
def generate_tours():
    min_cost = float_info.max
    best_tour = None
    
    for city_subset in itertools.combinations(range(1, 15), 11):  # Combinations of 11 cities excluding depot (0)
        full_tour = [0] + list(city_subset) + [0]  # Forming the full tour
        tour_cost = 0
        
        # Calculate the cost of the potential tour
        for i in range(len(full_tour) - 1):
            tour_cost += euclidean_distance(full_tour[i], full_tour[i+1])

        # Update the best tour found
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = full_tour
    
    return best_tour, min_cost

# Retrieve the best tour and its total cost
best_tour, min_cost = generate_tours()

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)