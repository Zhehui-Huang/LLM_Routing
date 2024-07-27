import math
import itertools

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Generate initial tour using the nearest neighbor heuristic
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    tour = [start]
    current = start
    unvisited.remove(start)

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current, x))
        tour.append(next_city)
        current = next_world = next_city
        unvisited.remove(next_city)

    tour.append(start)  # Return to depot
    return tour

# Calculate the cost of the tour
def tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# 2-opt optimization to improve the tour
def optimize_tour(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour)):
                if j - i == 1: continue  # these are consecutive edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_cost(new_tour) < tour_cost(tour):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour

# Create and optimize the tour
initial_tour = nearest_neighbor_tour(0)
optimized_tour = optimize_tour(initial_tour)
final_cost = tour_cost(optimized_tour)

# Output the results
print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {final_cost:.2f}")