import math
import itertools

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(cities, start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start)  # return to depot
    return tour

def two_opt(route, cities):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # these are consecutive cities
                new_route = route[:]
                new_route[i:j] = route[j - 1:i - 1:-1]  # reverse the segment between i and j
                if route_cost(new_route, cities) < route_cost(best, cities):
                    best = new_route
                    improved = True
        route = best
    return best

def route_cost(route, cities):
    cost = 0
    for i in range(1, len(route)):
        cost += euclidean_distance(cities[route[i - 1]], cities[route[i]])
    return cost

# Define coordinates of each city
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

initial_tour = nearest_neighbor_tour(cities, 0)
optimized_tour = two_opt(initial_tour, cities)
total_cost = route_cost(optimized_tour, cities)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost}")