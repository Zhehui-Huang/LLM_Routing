import math
import random

# City coordinates
coordinates = [
    (35, 40),  # depot city 0
    (39, 41),  # city 1
    (81, 30),  # city 2
    (5, 50),   # city 3
    (72, 90),  # city 4
    (54, 46),  # city 5
    (8, 70),   # city 6
    (97, 62),  # city 7
    (14, 41),  # city 8
    (70, 44),  # city 9
    (27, 47),  # city 10
    (41, 74),  # city 11
    (53, 80),  # city 12
    (21, 21),  # city 13
    (12, 39)   # city 14
]

# City groups
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

def random_initial_tour():
    tour = [0]  # Start at the depot
    selected_cities = []
    for group in groups:
        selected_city = random.choice(group)
        selected_cities.append(selected_city)
    random.shuffle(selected_cities)  # To add randomness to the initial tour
    tour.extend(selected_cities)
    tour.append(0)  # Return to the depot
    return tour

def calculate_total_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

def local_optimization(tour):
    """Simple 2-opt optimization as local optimization step."""
    improved = True
    while improved:
        improved = False
        best_cost = calculate_total_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # neighbors, no need to swap
                new_tour = tour[:]
                new_tour[i:j] = tour[j-1:i-1:-1]  # reverse the segment between i and j
                new_cost = calculate_total_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
    return tour

def find_best_tour():
    best_tour = None
    best_cost = float('inf')
    for _ in range(1000):  # number of trials
        tour = random_initial_tour()
        tour = local_optimization(tour)
        cost = calculate_total_cost(tour)
        if cost < best_cost:
            best_tour = tour
            best_cost = cost
    return best_tour, best_cost

best_tour, best_cost = find_best_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")