import itertools
from math import sqrt

# Distance calculation function
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = [
    (30, 56),  # City 0: Depot
    (53, 42),  # City 1
    (1, 95),   # City 2
    (25, 61),  # City 3
    (69, 57),  # City 4
    (6, 58),   # City 5
    (12, 84),  # City 6
    (72, 77),  # City 7
    (98, 95),  # City 8
    (11, 0),   # City 9
    (61, 25),  # City 10
    (52, 0),   # City 11
    (60, 95),  # City 12
    (10, 94),  # City 13
    (96, 73),  # City 14
    (14, 47),  # City 15
    (18, 16),  # City 16
    (4, 43),   # City 17
    (53, 76),  # City 18
    (19, 72)   # City 19
]

# Nearest neighbor heuristic
def nearest_neighbor(cities, start, num_cities):
    unvisited = set(range(len(cities)))
    unvisited.remove(start)
    tour = [start]
    current = start

    while len(tour) < num_cities:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        unvisited.remove(next_city)
        tour.append(next_city)
        current = next_city
    tour.append(start)  # return to the start
    return tour

# 2-opt optimization
def two_opt(route, cities):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 1):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # reverse segment
                
                if route_length(new_route, cities) < route_length(best, cities):
                    best = new、_route
                    improved = True
        route = best
    return best

def route_length(route, cities):
    return sum(euclidean_distance(cities[route[i]], cities[route[i - 1]]) for i in range(1, len(route)))

# Heuristic execution
initial_tour = nearest_neighbor(cities, 0, 13)
optimized_tour = two_opt(initial_tour, cities)
total_cost = route_length(optimized_tour, cities)

print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)