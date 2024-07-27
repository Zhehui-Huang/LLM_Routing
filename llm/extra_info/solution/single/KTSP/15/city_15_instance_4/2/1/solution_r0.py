from itertools import combinations, permutations
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def find_shortest_tour(cities):
    # Store positions
    positions = [
        (35, 40), (39, 41), (81, 30), (5, 50), 
        (72, 90), (54, 46), (8, 70), (97, 62),
        (14, 41), (70, 44), (27, 47), (41, 74),
        (53, 80), (21, 21), (12, 39)
    ]
    
    min_cost = float('inf')
    best_tour = []
    
    # Choose 11 cities (excluding depot) to visit from 14 options (cities[1:]).
    for subset in combinations(range(1, 15), 11):
        # Include depot city at the start and end.
        # Full loop tour permutation:
        current_cities = [0] + list(subset) + [0]
        
        # Iterate through all permutations of the inner cities.
        for perm in permutations(subset):
            perm_cities = [0] + list(perm) + [0]
            total_cost = 0
            for i in range(len(perm_cities) - 1):
                total_cost += euclidean_distance(positions[perm_cities[i]], positions[perm_cities[i + 1]])
            
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour = perm_cities
    
    return best_tour, min_cost

# Main Execution
tour, total_cost = find_shortest_tour(range(15))
print("Tour:", tour)
print("Total travel cost:", total_cost)