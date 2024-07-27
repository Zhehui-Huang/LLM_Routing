import random
import math
from itertools import permutations

cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def tour_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i - 1]]) for i in range(len(tour)))

def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    
    city_indices = list(cities.keys())
    
    for _ in range(10):  # Multi-start approach, start multiple independent trials
        # Step 1: Random subset selection
        random_subset = random.sample(city_indices[1:], 11)  # Select 11 cities randomly, excluding the depot
        random_subset = [0] + random_subset  # Add the depot city to the list
        
        # Step 2: Try all permutations of the selected cities subset
        all_permutations = permutations(random_subset)
        for perm in all_permutations:
            perm = list(perm) + [0]  # Ensure it returns to the starting city
            cost = tour_distance(perm)
            if cost < best_cost:
                best_cost = cost
                best_tour = perm
    
    return best_tour, best_cost

best_tour, total_cost = find_best_tour()

print("Tour:", best_tour)
print("Total travel cost:", round(total_cost, 2))