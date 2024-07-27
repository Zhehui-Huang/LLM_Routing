import math
import itertools

# City coordinates as (city_index: (x, y))
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46),
    6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47),
    11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Euclidean distance calculation
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix calculation
distance_matrix = {}
for i in cities:
    for j in cities:
        if i != j:
            distance_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

# Initial tour generation (naive)
def initial_tour():
    unvisited = list(cities.keys())[1:]  # Skip the depot initially
    current_city = 0
    tour = [0]  # Start at the depot

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[(current_city, city)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_id

    tour.append(0)  # Return to the depot
    return tour

# Tour cost calculation
def calculate_tour_cost(tour):
    total_cost = sum(distance_matrix[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    return total_cost

# Applying the initial tour
tour = initial_tour()
total_cost = calculate_tour_cost(tour)
print("Tour:", tour)
print("Total travel cost:", total_cost)

# TODO: Implement Lin-Kernighan heuristic improvements on the tour
# This requires a deeper implementation considering time and space complexity.