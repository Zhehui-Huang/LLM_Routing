import math
from random import shuffle

def euclidean_distance(c1, c2):
    return math.hypot(c1[0] - c2[0], c1[1] - c2[1])

def create_initial_tour(num_cities):
    tour = list(range(num_cities))
    shuffle(tour)
    tour.append(tour[0])  # Return to depot
    return tour

def calculate_tour_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total