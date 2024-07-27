import math
from itertools import permutations

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates for each city by index
cities = {
    0: (8, 11), 
    1: (40, 6), 
    2: (95, 33), 
    3: (80, 60), 
    4: (25, 18), 
    5: (67, 23), 
    6: (97, 32), 
    7: (25, 71), 
    8: (61, 16),
    9: (27, 91), 
    10: (91, 46), 
    11: (40, 87), 
    12: (20, 97), 
    13: (61, 25), 
    14: (5, 59), 
    15: (62, 88), 
    16: (13, 43), 
    17: (61, 28), 
    18: (60, 63), 
    19: (93, 15)
}

# Use the 2-opt algorithm to improve tour iteratively
def two_opt(cities, initial_tour):
    best = initial_tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 2, len(best)):
                if j - i == 1: 
                    continue  # Skip adjacent edges as they cannot be swapped
                new_tour = best[:i] + best[i:j][::-1] + best[j:]
                if tour_cost(cities, new_tour) < tour_cost(cities, best):
                    best = new_tours
                    improved = True
    return best

def tour_cost(cities, tour):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(cities[tour[i - 1]], cities[tour[i]])
    total_cost += calculate_distance(cities[tour[-1]], cities[tour[0]])  # Return to the depot
    return total_cost

# Nearest Neighbor initial heuristic tour
def nearest_neighbor_tour(cities, start):
    unvisited = set(cities.keys())
    tour = [start]
    unvisited.remove(start)
    while unoccupied:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: calculate_distance(cities[last], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)
    return tour

initial_tour = nearest_neighbor_tour(cities, 0)
optimized_tour = two_opt(cities, initial_tour)
total_cost = tour_cost(cities, optimized_tour)

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)