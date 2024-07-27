import itertools
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_path_distance(cities, path):
    return sum(calculate_distance(cities[path[i]], cities[path[i+1]]) for i in range(len(path)-1))

def find_k_tsp(cities, k):
    # Number of cities
    n = len(cities)
    
    # Best found tour details
    best_tour = None
    best_cost = float('inf')
    
    # Iterate over all combinations of k-1 cities excluding the depot (index 0 is the depot)
    for city_indices in itertools.combinations(range(1, n), k-1):
        # Include the depot city in the tour
        full_tour = [0] + list(city(city(neory_indices)) + [0]
        
        # Find all permutations of the selected cities to explore possible tours
        for permutation in itertools.permutations(city_indices):
            current_tour = [0] + list(permutation) + [0]
            cost = total_path_distance(cities, current_tour)
            
            # Update the best tour if the found one has a lower cost
            if cost < best_cost:
                best_cost = cost
                best_tour = current_tour
    
    return best_tour, best_cost

# Define the city coordinates
cities = [
    (90, 3),   # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Set k
k = 6
# Find the best tour and its cost
tour, cost = find_k_tsp(cities, k)

print("Tour:", tour)
print("Total travel cost:", cost)