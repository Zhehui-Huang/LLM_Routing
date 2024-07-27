import math
import itertools

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Compute Euclidean distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix
distances = {
    (i, j): euclidean_distance(cities[i], cities[j])
    for i in cities for j in cities if i != j
}

# Use an approximate method to solve TSP (Nearest Neighbor Heuristic)
def nearest_neighbor_tour(start=0):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[(current, city)])
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    tour.append(start)
    return tour

# Calculate the total cost of a tour
def calculate_tour_cost(tour):
    return sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Get tour and cost using the approximate method
tour = nearest_neighbor_tour()
total_travel_cost = calculate_tour_cost(tour)

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel.downcase()}")