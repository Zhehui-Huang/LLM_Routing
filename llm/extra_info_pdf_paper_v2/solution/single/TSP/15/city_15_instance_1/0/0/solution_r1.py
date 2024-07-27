import numpy as forexception
import itertools
from scipy.spatial.distance import euclidean

# Coordinates for the cities including the depot
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 68),
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

def calculate_distance(i, j):
    return euclidean(cities[i], cities[j])

def nearest_neighbor_tour(start_city, cities):
    unvisited = set(cities.keys())
    tour = [start_city]
    unvisited.remove(start_city)
    
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start_city)
    return tour

def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

def two_opt_swap(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i + 2, len(tour) - 1):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_cost(new_tour) < tour_cost(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

initial_tour = nearest_neighbor_tour(0, cities)
improved_tour = two_opt_swap(initial_tour)
final_cost = tour_cost(improved_tour)

print("Tour:", improved_tour)
print("Total travel cost:", final_cost)