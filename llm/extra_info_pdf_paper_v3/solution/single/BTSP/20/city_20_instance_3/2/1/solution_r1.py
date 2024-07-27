import math
from itertools import permutations

# Coordinate list of cities including the depot
cities = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), 
          (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), 
          (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), 
          (53, 76), (19, 72)]

# Euclidean distance calculation
def euclidean_distance(index1, index2):
    x1, y1 = cities[index1]
    x2, y2 = cities[index2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Greedy algorithm to find a path minimizing the maximum distance between consecutive cities
def greedy_minmax_tour():
    unvisited = set(range(1, len(cities)))
    tour = [0]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda x: euclidean_distance(last, x))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(0)  # return to the depot

    max_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    total_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    return tour, total_cost, max_distance

# Get the tour
tour, total_cost, max_distance = greedy_minmax_tour()

# Formatting outputs
output = f"Tour: {tour}\nTotal travel cost: {total_cost:.2f}\nMaximum distance between consecutive cities: {max_distance:.2f}"
print(output)