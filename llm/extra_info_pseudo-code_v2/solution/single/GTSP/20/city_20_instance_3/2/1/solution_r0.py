import random
import math
import sys

# Defining the city coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Groups of cities
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

# Generate initial feasible random tour
def initial_tour():
    tour = [0]
    for group in groups:
        tour.append(random.choice(group))
    tour.append(0)
    return tour

# Calculate the total tour cost
def calculate_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

# Find a random neighbor tour
def random_neighbor(tour):
    new_tour = tour[1:-1]
    group_index = random.randint(0, 5)  # choose a random group
    new_city = random.choice(groups[group_index])
    while new_city in new_tour:
        new_city = random.choice(groups[group_index])
    new_tour[group_index - 1] = new_city
    return [0] + new_tour + [0]

# Simulated annealing to find the best tour
def simulated_annealing():
    current_tour = initial_tour()
    current_cost = calculate_cost(current_tour)
    best_tour = current_tour
    best_cost = current_cost
    T = 1000
    cooling_rate = 0.995
    min_temperature = 1

    while T > min_temperature:
        new_tour = random_neighbor(current_tour)
        new_cost = calculate_weight(new_tour)
        if new_cost < best_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / T):
            current_tour = new_tour
            current_cost = new_cost
            if new_cost < best_cost:
                best_tour = new_tour
                best_cost = new_cost
        T *= cooling_rate

    return best_tour, best_cost

# Execute
best_tour, best_cost = simulated_annealing()
print("Tour:", best_tour)
print("Total travel cost:", best_cost)