import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Measure all distances between cities in advance
distance_matrix = {}
for i in cities:
    for j in cities:
        distance_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

def calculate_tour_cost(tour):
    total_cost = distance_matrix[(0, tour[0])]
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[(tour[i], tour[i+1])]
    total_cost += distance_matrix[(tour[-1], 0)]
    return total_cost

def find_shortest_tour():
    all_combinations = list(permutations([group[0] for group in groups]))
    best_tour = None
    min_cost = float('inf')
    
    for combination in all_combinations:
        cost = calculate_tour_cost(combination)
        if cost < min_cost:
            min_cost = cost
            best_tour = combination
    
    return best_tour, min_cost

best_tour, min_cost = find_shortest_tour()
complete_tour = [0] + list(best_tour) + [0]

print("Tour:", complete_tour)
print("Total travel cost:", min_cost)