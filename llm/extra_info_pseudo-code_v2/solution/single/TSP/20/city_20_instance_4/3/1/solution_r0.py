import math
from itertools import permutations

# Define cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Provide an initial feasible solution - Nearest Neighbor
def nearest_neighbor_tour(start, cities):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current], cities[city]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(start)  # return to the start
    return tour

# Calculate the cost of the tour
def tour_cost(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Given a tour, generates all possible 2-opt neighbors
def get_2opt_neighbors(tour):
    neighbors = []
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            neighbor = tour[:]
            neighbor[i:j+1] = reversed(neighbor[i:j+1])
            neighbors.append(neighbor)
    return neighbors

# Perform the 2-opt local search
def two_opt(tour, cities):
    improvement = True
    while improvement:
        improvement = False
        best_cost = tour_cost(tour, cities)
        for neighbor in get_2opt_neighbors(tour):
            current_cost = tour_cost(neighbor, cities)
            if current_cost < best_cost:
                tour = neighbor
                best_cost = current_cost
                improvement = True
    return tour

# Main execution process
initial_tour = nearest_neighbor_tour(0, cities)
improved_tour = two_opt(initial_tour, cities)
final_cost = tour_cost(improved_tour, cities)

print("Tour:", improved_tour)
print("Total travel cost:", final_cost)