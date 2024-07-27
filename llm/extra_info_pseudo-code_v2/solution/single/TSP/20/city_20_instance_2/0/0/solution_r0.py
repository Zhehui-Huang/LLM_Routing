import math
from itertools import permutations

# City coordinates as provided
cities = [
    (3, 26),   # depot city 0
    (85, 72),  # city 1
    (67, 0),   # city 2
    (50, 99),  # city 3
    (61, 89),  # city 4
    (91, 56),  # city 5
    (2, 65),   # city 6
    (38, 68),  # city 7
    (3, 92),   # city 8
    (59, 8),   # city 9
    (30, 88),  # city 10
    (30, 53),  # city 11
    (11, 14),  # city 12
    (52, 49),  # city 13
    (18, 49),  # city 14
    (64, 41),  # city 15
    (28, 49),  # city 16
    (91, 94),  # city 17
    (51, 58),  # city 18
    (30, 48)   # city 19
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Generate an initial naive tour (nearest neighbor heuristic)
def nearest_neighbor_tour(start, cities):
    tour = [start]
    unvisited = set(range(len(cities))) - {start}
    current_city = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start)  # return to depot
    return tour

# Simple Lin-Kernighan-like improvement (a 2-opt swap)
def two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                if j - i == 1: continue  # Skip adjacent edges
                if total_distance(tour[:i+1] + tour[i+1:j+1][::-1] + tour[j+1:]) < total_distance(tour):
                    tour = tour[:i+1] + tour[i+1:j+1][::-1] + tour[j+1:]
                    improvement = True
    return tour

# Start finding the optimal tour
initial_tour = nearest_neighbor_tour(0, cities)
improved_tour = two_opt(initial_tour)
total_cost = total_tour_length(improved_tour)

# Output the result
print(f"Tour: {improved_tour}")
print(f"Total travel cost: {total_cost}")