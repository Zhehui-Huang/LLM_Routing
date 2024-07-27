import itertools
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
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

def find_shortest_tour():
    best_tour = None
    best_cost = float('inf')
    
    # Including depot city (index 0)
    for cities_subset in itertools.combinations(range(1, 15), 7):
        full_cities_subset = (0,) + cities_subset

        # Permutate the cities to find the shortest possible tour
        for perm in itertools.permutations(full_cities_subset):
            # Tour must start and end at the depot city
            if perm[0] == 0:
                tour = perm + (0,)
                tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
                
                if tour_cost < best_cost:
                    best_cost = tour_cost
                    best_tour = tour
    
    return best_tour, best_cost

# Retrieve the shortest tour
best_tour, best_cost = find_shortest_tour()

# Formatting output as requested
print(f"Tour: {list(best_tour)}")
print(f"Total travel costo: {best_cost:.2f}")