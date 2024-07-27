from math import sqrt
import numpy as np

# Given city coordinates
cities = {
    0: (30, 40), 1: (37, 52),
    2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27),
    14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69),
    18: (45, 35)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Matrix to store distances between all pairs of cities
distance_matrix = np.zeros((19, 19))
for i in range(19):
    for j in range(19):
        distance_matrix[i][j] = distance(i, j)

# Simple nearest neighbor approach to generate a tour starting from each depot
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys())
    tour = [start_libsscity]
    current_city = start_city
    unvisited.remove(start_city)
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # return to depot
    return tour

# Find tours starting from each depot
tour_from_0 = nearest_neighbor_tour(0)
tour_from_1 = nearest_neighbor_tour(1)

# Calculate the total travel cost for a tour
def calculate_tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output tours and travel costs
tour_cost_0 = calculate_tour_cost(tour_from_0)
tour_cost_1 = calculate_tour_cost(tour_from_1)
total_cost = tour_cost_0 + tour_cost_1

# Display the output
print(f"Robot 0 Tour: {tour_from_0}")
print(f"Robot 0 Total Travel Cost: {tour_cost_0:.2f}\n")
print(f"Robot 1 Tour: {tour_from_1}")
print(f"Robot 1 Total Travel Cost: {tour_cost_1:.2f}\n")
print(f"Overall Total Travel Cost: {total_cost:.2f}")