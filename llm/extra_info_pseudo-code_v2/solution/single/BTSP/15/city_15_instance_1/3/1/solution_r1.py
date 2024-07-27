import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_tour(cities):
    num_cities = len(cities)
    all_permutations = permutations(range(num_cities))
    best_tot_cost = float('inf')
    best_tour = []
    best_max_dist = float('inf')

    for perm in all_permutations:
        if perm[0] == 0:  # Ensuring tour starts and ends at depot
            current_cost = 0
            max_dist = 0
            valid_tour = True
        
            for i in range(1, len(perm)):
                dist = euclidean_distance(cities[perm[i - 1]], cities[perm[i]])
                current_cost += dist
                if dist > max_dist:
                    max_dist = dist
            
            dist = euclidean_distance(cities[perm[-1]], cities[perm[0]])
            current_cost += dist
            if dist > max_dist:
                max_dist = dist

            if max_dist < best_max_dist:
                best_max_dist = max_dist
                best_tot_cost = current_cost
                best_tour = list(perm) + [0]

    return best_tour, best_tot_cost, best_max_dist

# Defining the cities coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
          (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
          (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

best_tour, best_total_cost, best_max_distance = find_tour(cities)

# Print results
print("Tour:", best_tour)
print("Total travel cost:", best_total_cost)
print("Maximum distance between consecutive cities:", best_max_distance)