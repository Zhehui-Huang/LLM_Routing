import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = [
    (8, 11),   # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

def find_best_tour():
    best_distance = float('inf')
    best_tour = None
    # Consider depot and other cities separately
    depot = cities[0]
    other_cities = cities[1:]
    
    # Generate all combinations of 3 cities from other cities since including the depot
    for combo in itertools.combinations(other_cities, 3):
        current_cities = [depot] + list(combo)
        # Check all permutations of the chosen cities
        for perm in itertools.permutations(current_cities):
            if perm[0] == depot:  # make sure the tour starts and ends at the depot
                # Calculate the tour distance
                tour_distance = sum(euclidean_distance(perm[i], perm[i+1]) for i in range(len(perm) - 1))
                tour_distance += euclidean_distance(perm[-1], perm[0])  # close the tour
                # Update the best tour found
                if tour_distance < best_distance:
                    best_distance = tour_distance
                    best_tour = perm
    
    # Convert the best tour into city indices
    best_tour_indices = [cities.index(city) for city in best_tour] + [0]  # Add the depot to complete the cycle
    return best_tour_indices, best_distance

tour, total_cost = find_best_tour()
print("Tour:", tour)
print("Total travel cost:", total_cost)