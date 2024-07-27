import itertools
from math import sqrt
from sys import maxsize

# Define the cities coordinates.
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Distance calculation function
def calculate_distance(index1, index2):
    return sqrt((cities[index1][0] - cities[index2][0])**2 + (cities[index1][1] - cities[index2][1])**2)

# Identify the shortest route from a starting index using a greedy algorithm.
def find_shortest_route(start_index, indices):
    path = [start_index]
    current_index = start_index
    total_distance = 0

    while indices:
        next_index = min(indices, key=lambda x: calculate_distance(x, current_index))
        total_distance += calculate_distance(current_index, next_index)
        path.append(next_index)
        indices.remove(next_index)
        current_ucity = next_index

    # Return to the start
    total_distance += calculate_distance(path[-1], start_index)
    path.append(start_index)
    return path, total_distance

# Main part of the function that attempts to find the best route
def optimal_tour():
    min_distance = maxsize
    best_path = []
    city_indices = list(range(1, 15))

    # Consider all combinations of 11 cities to visit along with the start
    for subset in itertools.combinations(city_indices, 11):
        tour, distance = find_shortest_route(0, list(subset))
        if distance < min_distance:
            min_distance = distance
            best_path = tour

    return best_path, min_distance

# Execute the function and print the outputs
tour, total_cost = optimal_tour()
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))