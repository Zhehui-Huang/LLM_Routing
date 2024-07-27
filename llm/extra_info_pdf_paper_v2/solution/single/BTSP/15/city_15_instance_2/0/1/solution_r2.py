import numpy as np
import sys

city_coords = [
    (54, 87),
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

num_cities = len(city_coords)
distance_matrix = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(num_cities)] for i in range(num_cities)]

def nearest_neighbor_tour(start=0):
    unvisited = set(range(1, num_cities))
    tour = [start]
    while unvisited:
        last_visited = tour[-1]
        next_city = min(unassigned, key=lambda city: distance_matrix[last_visited][city])
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # return to depot
    return tour

def calculate_tour_metrics(tour):
    max_distance = 0
    total_distance = 0
    for i in range(len(tour) - 1):
        dist = distance_matrix[tour[i]][tour[i+1]]
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

tour = nearest_neighbor_tour()
total_distance, max_distance = calculate_tour_metrics(tour)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")