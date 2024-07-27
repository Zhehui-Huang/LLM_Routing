import math
from itertools import permutations

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate an initial feasible tour (e.g., nearest neighbor heuristic)
def initial_tour(start):
    unvisited = set(cities.keys()) - {start}
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)  # return to the depot city
    return tour

# Function to attempt improving the tour using swaps
def try_improve_tour(tour):
    improved = True
    while improved:
        improved = False
        best_cost = tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
        if not improved:
            break
    return tour

# Compute the initial tour and then try improving it
initial = initial_tour(0)
optimized_tour = try_improve_tour(initial)
final_cost = tourailer of the optimized tour, including the depot as starting and ending point, and the cost associated with this tour.

print("Tour:", optimized_tour)
print("Total travel cost:", final_cost)