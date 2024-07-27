import math
import itertools

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def initial_tour(cities):
    # Start at the depot, and use nearest neighbor heuristic to generate an initial tour
    n = len(cities)
    unvisited = set(range(1, n))
    current = 0
    tour = [0]

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current], cities[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(0)  # returning to the depot
    return tour

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    return total_cost

def simple_lin_kernighan(tour, cities):
    # Since this problem is for solving an example, a simple implementation of LK is presented
    # This does not fully implement the LK heuristic, but demonstrates a spirit of local search.

    def generate_pairs(n):
        return [(i, j) for i in range(n) for j in range(n) if i != j]

    improved = True
    best_cost = calculate_total_cost(tour, cities)
    best_tour = tour[:]

    while improved:
        improved = False
        pairs = generate_pairs(len(tour) - 1)  # don't include the last return to depot in pairs
        for i, j in pairs:
            if abs(i - j) <= 1:  # they must not be consecutive
                continue
            new_tour = best_tour[:min(i, j) + 1] + best_tour[min(i, j) + 1:max(i, j) + 1][::-1] + best_tour[max(i, j) + 1:]
            new_cost = calculate_total_cost(new_tour, cities)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour[:]
                improved = True

    return best_tour, best_cost

# Cities' coordinates [depot (0), cities 1-9]
cities = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]

# Obtain an initial tour
initial = initial_tour(cities)

# Try to improve the tour using a simplified Lin-Kernighan heuristic
lk_tour, lk_cost = simple_lin_kernighan(initial, cities)

print("Tour:", lk_tour)
print("Total travel cost:", lk_cost)