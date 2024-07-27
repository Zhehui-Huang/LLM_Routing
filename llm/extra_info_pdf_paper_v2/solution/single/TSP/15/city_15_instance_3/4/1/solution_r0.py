import math
from itertools import permutations

# Define cities by their coordinates
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Helper function to calculate Euclidean distance
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Prepare the distance matrix
n = len(cities)
dist_matrix = [[calc_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Generate initial tour using a simple heuristic (nearest neighbor)
def initial_tour():
    unvisited = set(range(1, n))
    tour = [0]  # start at the depot city 0
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current][x])
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(0)  # return to the depot
    return tour

# Calculate total travel cost
def tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Swap two edges to find a possible better tour (2-opt)
def two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue
                if dist_matrix[tour[i - 1]][tour[i]] + dist_matrix[tour[j]][tour[j + 1]] > dist_matrix[tour[i - 1]][tour[j]] + dist_matrix[tour[i]][tour[j + 1]]:
                    # More optimal to swap
                    tour[i:j + 1] = reversed(tour[i:j + 1])
                    improvement = True
    return tour

def solve_tsp():
    tour = initial_tour()
    tour = two_opt(tour)
    total_cost = tour_cost(tour)
    return tour, total_cost

# Solve the problem
final_tour, final_cost = solve_tsp()

# Display the results
print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))