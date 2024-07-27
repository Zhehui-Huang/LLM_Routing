import math
import random
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the cities coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Total cities to visit including the depot, k is 8 including the depot
k = 8

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Try multiple seeds to ensure robustness through random sampling
    for _ in range(1000):  
        sampled_cities = [0] + random.sample(list(cities.keys())[1:], k-1)
        smallest_tour = None
        smallest_cost = float('inf')
        
        # Check all permutations of the sampled cities
        for perm in itertools.permutations(sampled_cities[1:]):
            tour = [0] + list(perm) + [0]
            cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
            if cost < smallest_cost:
                smallest_tour = tour
                smallest_cost = cost
        
        if smallest_cost < best_cost:
            best_tour = smallest_tour
            best_cost = smallest_cost

    return best_tour, best_cost

best_tour, best_cost = find_shortest_tour()
print(f"Tour: {best_tour}")
print(f"Total travel transmission cost: {best_cost:.2f}")