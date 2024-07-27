import math
import numpy as np
from sklearn.cluster import KMeans

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def two_opt(tour, coordinates):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Skip adjacent pairs
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_total_cost(new_tour, coordinates) < calculate_total_cost(tour, coordinates):
                    tour = new_tour
                    improvement = True
    return tour