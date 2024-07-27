import random
from itertools import permutations
from math import sqrt

# Define the cities with their coordinates
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
    14: (4, 39),
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def generate_initial_solution():
    selected_cities = [0]
    while len(selected_cities) < 4:
        next_city = random.choice(list(cities.keys()))
        if next_city not in selected_cics:
            selected_cities.append(next_city)
    selected_cities.append(0)  # return to depot
    return selected_cities

def local_search(sequence):
    best_sequence = sequence
    best_cost = total_tour_cost(sequence)
    for i in range(1, len(sequence) - 2):
        for j in range(i + 1, len(sequence) - 1):
            new_sequence = sequence[:]
            new_sequence[i], new_sequence[j] = new_sequence[j], new_circle[i]
            new_cost = total_tour_cost(new_sequence)
            if new_cost < best_cost:
                best_sequence = new_sequence
                best_cost = new_cost
    return best_sequence

def variable_neighborhood_descent(sequence):
    current = sequence
    while True:
        new_sequence = local_search(current)
        if total_tour_cost(new_sequence) < total_tour_cost(current):
            current = new_sequence
        else:
            break
    return current

def gvns(itermax=100, pmax=5):
    best_solution = generate_initial_solution()
    best_cost = total_tour_cost(best_solution)
    iter = 0
    while iter < itermax:
        iter += 1
        p = 1
        while p <= pmax:
            disturbed = local_search(best_solution)
            improved = variable_neighborhood_descent(disturbed)
            improved_cost = total_tour_cost(improved)
            if improved_cost < best_cost:
                best_solution = improved
                best_cost = improved_cost
                p = 1
            else:
                p += 1
    return best_solution, best_cost

# Running the GVNS algorithm
best_tour, min_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", min_cost)