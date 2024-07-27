import math
from itertools import product

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor_tour(cities):
    unvisited = set(cities.keys())
    current = 0
    tour = [0]
    unvisited.remove(0)
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(0)
    return tour

def total_cost(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

def two_opt(tour, cities):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if total_cost(new_tour, cities) < total_cost(best, cities):
                    best = new_tour
                    improved = True
        tour = best
    return best

# Define city coordinates
cities = {0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
          5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
          10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)}

# Find the initial tour using Nearest Neighbor algorithm
init_tour = nearest_neighbor_tour(cities)

# Optimize the tour using the 2-opt algorithm
optimized_tour = two_opt(init_tour, cities)

# Calculate the total travel cost of the optimized tour
cost = total_cost(optimized_tour, cities)

# Output the tour and total cost
print("Tour:", optimized_tour)
print("Total travel cost:", cost)