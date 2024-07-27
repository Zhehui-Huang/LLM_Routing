import itertools
from math import sqrt

# Define a function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Given city coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Function to find a route using a greedy nearest neighbor heuristic
def nearest_neighbor(start, cities_indices):
    unvisited = cities_indices[:]
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unkept, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        unvisited.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    tour.append(start)  # Return to the starting city
    return tour

# Function to compute the total path distance of a tour
def tour_distance(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total distance

# Consider all combinations of 11 other cities (excluding depot city)
best_tour = None
min_distance = float('inf')
city_indices = list(range(1, 15))  # list of city indices excluding the depot

for subset in list(itertools.combinations(city_indices, 11)):
    attempt_tour = nearest_neighbor(0, list(subset))
    attempt_distance = tour_distance(attempt_tour)

    if attempt_distance < min_distance:
        best_tour = attempt_tour
        min_distance = attempt_distance

# Output
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))