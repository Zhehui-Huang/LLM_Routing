import math
import random

# Coordinates of the cities
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Precompute distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

def get_tour_cost(tour):
    cost = 0
    max_leg = 0
    for i in range(len(tour) - 1):
        leg = distances[(tour[i], tour[i+1])]
        cost += leg
        if leg > max_leg:
            max_leg = leg
    return cost, max_leg

# Start with a simple nearest neighbor tour
def nearest_neighbor(start=0):
    current = start
    unvisited = set(cities.keys()) - {start}
    tour = [start]
    while unvisited:
        next_city = min(unvisited, key=lambda x: distances[(current, x)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)
    return tour

# Iterative improvement (optimizing the tour by tweaking the legs)
def optimize_tour(tour):
    min_cost, min_max_leg = get_tour_cost(tour)
    best_tour = tour[:]
    for i in range(10000):  # number of iterations
        # Swap two cities in the tour (excluding the start/end city)
        a, b = random.randint(1, len(cities)-2), random.randint(1, len(cities)-2)
        if a != b:
            new_tour = best_tour[:]
            new_tour[a], new_tour[b] = new_tour[b], new_tour[a]
            cost, max_leg = get_tour_cost(new_tour)
            if max_leg < min_max_leg:
                best_tour = new_tour
                min_cost, min_max_leg = cost, max_leg
    return best_tour, min_cost, min_max_leg

# Compute an initial solution
init_tour = nearest_neighbor()

# Optimize the tour
optimized_tour, total_cost, max_distance = optimize_tour(init_tour)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")