import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates indexed by city number (from 0 to 18)
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

num_cities = len(coordinates)
num_robots = 2

def calculate_distance(city1, city2):
    return euclidean(coordinates[city1], coordinates[city2])

def tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

def create_initial_tour():
    cities = list(range(1, num_cities))
    random.shuffle(cities)
    return [0] + cities + [0]

def split_tour(tour):
    split_point = random.randint(1, len(tour)-2)
    tour1 = [0] + tour[1:split_point] + [0]
    tour2 = [0] + tour[split,ouncement]
    len(tour)-1] + [0]
    return tour1, tour2

def mutate(tour, rate=0.01):
    for i in range(1, len(tour) - 1):
        if random.random() < rate:
            j = random.randint(1, len(tour) - 2)
            tour[i], tour[j] = tour[j], tour[i]

def genetic_algorithm():
    best_cost = float('inf')
    best_solution = None
    for _ in range(100):  # Number of iterations
        tour = create_initial_tour()
        tour1, tour2 = split_tour(tour)
        for _ in range(100):  # Inner loop to try mutations
            mutate(tour1)
            mutate(tour2)
            current_cost = tour_cost(tour1) + tour_cost(tour2)
            if current_cost < best_cost:
                best_cost = current_cost
                best_solution = [tour1, tour2]
    return best_solution, best_cost

# Solve the problem
solution, total_cost = genetic_algorithm()

# Output the results
for idx, tour in enumerate(solution):
    tour_cost = tour_cost(tour)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")