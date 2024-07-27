import math
from itertools import permutations

# Define cities' coordinates
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate a list of all cities except the depot
cities_to_visit = list(cities.keys())
cities_to_visit.remove(0)

# Brute force solution to find the shortest tour
def find_shortest_tour():
    best_distance = float('inf')
    best_tour = None
    for perm in permutations(cities_to_visit):
        tour = [0] + list(perm) + [0]
        tour_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        if tour_distance < best_distance:
            best_distance = tour_distance
            best_tour = tour
    return best_tour, best_distance

# Find the shortest tour and its total distance
shortest_tour, total_distance = find_shortest_tour()

# Print the solution
print("Tour:", shortest_tour)
print("Total travel cost:", total_distance)