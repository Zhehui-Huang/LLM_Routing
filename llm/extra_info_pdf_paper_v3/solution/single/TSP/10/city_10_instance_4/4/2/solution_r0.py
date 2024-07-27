import math
import itertools

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26),
    4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70),
    8: (20, 99), 9: (66, 62)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Nearest Neighbour heuristic
def nearest_neighbour_tour(start, cities):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # return to the depot
    return tour

# Calculate total travel cost of the tour
def total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Find initial solution
tour = nearest_neighbour_tour(0, cities)
cost = total_travel_cost(tour, cities)

# Output the tour and total cost
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")