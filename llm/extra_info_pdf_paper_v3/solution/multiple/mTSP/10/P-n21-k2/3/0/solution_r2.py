import math
import numpy as np

# City coordinates (Depot city included as the first)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate the distance matrix between every pair of cities
num_cities = len(coordinates)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Basic nearest neighbour heuristic to generate initial solution
def nearest_neighbour_tour(start_city, cities_to_visit):
    tour = [start_city]
    current_city = start_city
    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda x: dist_matrix[current_city][x])
        tour.append(next_city)
        cities_to_visit.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # returning to the depot
    return tour

# Splitting cities semi-evenly among robots
cities_to_visit_1 = set(range(1, num_cities // 2 + 1))
cities_to_visit_2 = set(range(num_cities // 2 + 1, num_cities))

# Find tours for each robot
tour1 = nearest_neighbour_tour(0, cities_to_visit_1)
tour2 = nearest_neighbour_tour(0, cities_to_visit_2)

# Function to calculate the travel cost of a tour
def calculate_tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Calculate costs
cost1 = calculate_tour_cost(tour1)
cost2 = calculate_tour_cost(tour2)

# Output results
print(f"Robot 0 Tour: {tour1}")
print(f"Robot 0 Total Travel Cost: {cost1:.2f}")

print(f"Robot 1 Tour: {tour2}")
print(f"Robot 1 Total Travel Cost: {cost2:.2f}")

overall_cost = cost1 + cost2
print(f"Overall Total Travel Cost: {overall_cost:.2f}")