import math
import itertools

# City coordinates
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
    14: (98, 1)
}

# Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate the cost of a given route
def route_cost(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1))

# Find the shortest tour visiting exactly 6 cities including the depot (city 0)
def find_shortest_tour():
    all_cities = set(cities.keys())
    best_tour = None
    best_cost = float('inf')
    
    # Generate combinations of 5 other cities
    for combo in itertools.combinations(all_cities - {0}, 5):
        current_tour = [0] + list(combo) + [0]
        
        # Generate all permutations of the selected cities (excluding depot stays)
        for perm in itertools.permutations(combo):
            permuted_tour = [0] + list(perm) + [0]
            cost = route_cost(permuted_tour)
            
            if cost < best_cost:
                best_cost = cost
                best_tour = permuted_tour
                
    return best_tour, best_cost

# Get the shortest tour and its cost
tour, total_cost = find_shortest_tour()

# Output the result
output = f"Tour: {tour}\nTotal travel cost: {total_cost}"
print(output)