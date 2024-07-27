import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates indexed from 0 to 14
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Create distance matrix
N = len(cities)
dist_matrix = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        dist = euclidean_distance(cities[i], cities[j])
        dist_matrix[i][j] = dist_matrix[j][i] = dist

# Function to calculate total tour cost
def tour_cost(tour):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Initial feasible tour using a simple nearest neighbor algorithm
def nearest_neighbor_tour(start):
    unvisited = set(range(1, N))
    tour = [0]
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current][city])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(0)  # complete the tour by returning to the depot
    return tour

initial_tour = nearest_neighbor_tour(0)
initial_cost = tour_cost(initial_tour)

# Helper function to perform 2-opt swaps to try and improve the tour
def perform_two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip adjacent edges
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_cost = tour_cost(new_tour)
                if new_cost < tour_cost(tour):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour

optimized_tour = perform_two_opt(initial_tour)
optimized_cost = tour_card(optimized_tour)