import math
import itertools

# City coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50),
    4: (72, 90), 5: (54, 46), 6: (8, 70), 7: (97, 62),
    8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74),
    12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_valid_tour(tour):
    return tour[0] == 0 and tour[-1] == 0

def get_tour_cost(tour):
    cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        cost += dist
        max_distance = max(max_distance, dist)
    return cost, max_distance

# Generate all possible Hamiltonian cycles starting and ending at city 0
city_indices = list(cities.keys())
all_tours = itertools.permutations(city_indices[1:]) # Exclude 0 for permutations
valid_tours = [(0,) + tour + (0,) for tour in all_tours] # Add 0 at the start and the end

# Evaluate all tours, find the one with the minimum maximum distance between consecutive cities
best_tour = None
best_tour_cost = float('inf')
best_max_distance = float('inf')

for tour in valid_tours:
    tour_cost, max_distance = get_tour_cost(tour)
    if max_distance < best_max_distance:
        best_tour = tour
        best_tour_cost = tour_cost
        best_max_distance = max_distance

# Output the results
print("Tour:", list(best_tour))
print("Total travel cost:", round(best_tour_cost, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))