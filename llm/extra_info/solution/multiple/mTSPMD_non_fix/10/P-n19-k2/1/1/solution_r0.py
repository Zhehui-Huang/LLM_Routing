import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour, cities):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def nearest_neighbor(start, cities, unvisited):
    path = [start]
    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[last], cities[city]))
        path.append(next_city)
        unvisited.remove(next_city)
    return path

def two_opt(tour, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                if (euclidean_distance(cities[tour[i]], cities[tour[i - 1]]) + 
                    euclidean_distance(cities[tour[j]], cities[tour[j + 1]]) >
                    euclidean_distance(cities[tour[i]], cities[tour[j]]) + 
                    euclidean_distance(cities[tour[i - 1]], cities[tour[j + 1]])):
                    
                    tour[i:j + 1] = tour[j:i - 1:-1]
                    improved = True
    return tour

cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
          (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Assign depots
depot_0 = 0
depot_1 = 1

# Initial path optimization for both robots
remaining_cities = set(range(2, len(cities)))

tour_0 = nearest_neighbor(depot_0, cities, remaining_cities.copy())
tour_1 = nearest_neighbor(depot_1, cities, remaining_cities.difference(tour_0))

# Applying 2-opt heuristic for path improvement
optimized_tour_0 = two_opt(tour_0, cities)
optimized_tour_1 = two_opt(tour_1, cities)

# Calculate the distance of the tours
total_cost_0 = total_distance(optimized_tour_0, cities)
total_cost_1 = total_distance(optimized_tour_1, cities)

overall_total_cost = total_cost_0 + total_cost_1

# Print results
print(f"Robot 0 Tour: {optimized_tour_0}")
print(f"Robot 0 Total Travel Cost: {total_cost_0:.2f}\n")
print(f"Robot 1 Tour: {optimized_tour_1}")
print(f"Robot 1 Total Travel Cost: {total_cost_1:.2f}\n")
print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")