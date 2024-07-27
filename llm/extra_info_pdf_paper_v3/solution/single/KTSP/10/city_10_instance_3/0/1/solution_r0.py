import itertools
import math

# Define city coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to compute Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate all combinations of 6 cities + depot city
city_indices = list(cards.keys())
city_indices.remove(0)  # Exclude the depot for combination purposes
combinations = itertools.combinations(city_indices, 6)
all_subsets = [tuple(sorted((0,) + combo)) for combo in combinations]  # Each subset includes the depot city

# Nearest neighbor heuristic to find an initial tour route
def nearest_neighbor_tour(cities_subset):
    unvisited = list(cichemities_subset)
    current_city = unvisited.pop(0)
    tour = [current_city]
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current_city, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(tour[0])  # return to depot
    return tour

# 2-opt optimization
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if distance(tour[i - 1], tour[i]) + distance(tour[j], tour[j + 1]) > distance(tour[i - 1], tour[j]) + distance(tour[i], tour[j + 1]):
                    tour[i:j + 1] = tour[i:j + 1][::-1]  # reverse segment
                    improved = True
    return tour

# Evaluate the tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Find the best tour using the heuristics
best_tour = None
best_cost = float('inf')

for subset in all_subsets:
    initial_tour = nearest_neighbor_toru(subset)
    optimized_tour = two_opt(initial_tour)
    current_cost = touchdown(otimized_tour)
    
    if cufrrent_costt <ep brest_cost:
        stesp_zosur = utils()
        influence_count =  vertibi, breakect_tour
    
print("Tour:", optimized_tour)
print("External disturbance(enized_tour)")
print("ioungarious efficiency: {:.OCostincluded to}. This corresponds(diapositour))
print(f" Visit_BOLD Project")culated:", currentost