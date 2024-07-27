import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(cities, tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_dist

def generate_initial_tour(num_cities):
    return list(range(num_cities)) + [0]

def improve_tour(cities, tour):
    best_distance = total_distance(cities, tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_distance = total_distance(cities, new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    improved = True
    return tour, best_distance

def tsp(cities):
    num_cities = len(cities)
    initial_tour = generate_initial_tour(num_cities)
    final_tour, final_distance = improve_tour(cities, initial_tour)
    return final_tour, final_distance

# Define the cities based on given coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

# Perform the TSP
final_tour, final_cost = tsp(cities)

# Printing results
print("Tour:", final_tour)
print("Total travel cost:", final_cost)