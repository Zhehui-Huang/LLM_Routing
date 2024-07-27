import itertools
import math
import random

# City coordinates
city_coords = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Utility functions
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(city_coords[tour[i-1]], city_coords[tour[i]])
    total_cost += euclidean_distance(city_coords[tour[-1]], city_coords[tour[0]])  # Closing the loop
    return total_cost

# Select k - 1 cities (as 1 city is the depot) to form a tour with the depot city
k = 16
cities = list(city_coords.keys())

def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    iterations = 100
    
    for _ in range(iterations):
        selected_cities = random.sample(cities[1:], k-1)  # Select k-1 cities randomly, excluding the depot
        selected_cities = [0] + selected_cities           # Include depot city at the start and end
        
        # Explore all permutations of the selected cities and find the minimum cost possible
        for perm in itertools.permutations(selected_cities[1:]):
            current_tour = [0] + list(perm) + [0]
            current_cost = calculate_tour_cost(current_tour)
            if current_cost < best_cost:
                best_cost = current_cost
                best_tour = current_tour
    
    return best_tour, best_cost

best_tour, best_cost = find_best_tour()

print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))