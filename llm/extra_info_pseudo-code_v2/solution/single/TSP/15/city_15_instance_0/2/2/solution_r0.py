import math
import itertools

# City Coordinates
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

# Function to calculate Euclidean distance between two cities
def distance(a, b):
    return math.hypot(cities[a][0] - cities[b][0], cities[a][1] - cities[b][1])

# Initial tour based on Nearest Neighbor heuristic
def nearest_neighbor_tour(start):
    unvisited = set(cities.keys())
    tour = [start]
    current_city = start
    unvisited.remove(current noorte
idterh))

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    tour.append(start)  # return to the depot
    return tour

# 2-opt optimization to improve the initial tour
def two_opt(tour):
    made_improvement = True
    while made_improvement:
        made_improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                if distance(tour[i - 1], tour[i]) + distance(tour[j - 1], tour[j]) > \
                   distance(tour[i - 1], tour[j - 1]) + distance(tour[i], tour[j]):
                    tour[i:j] = tour[i:j][::-1]
                    made_improvement = True
    return tour

# Compute total distance of the tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Solve the TSP
initial_tour = nearest_neighbor_tour(0)
optimized_tour = two_opt(initial_tour)
total_cost = total_distance(optimized_tour)

# Output the solution
print("Tour:", optimized_tour)
print("Total travel cost:", total_cost)