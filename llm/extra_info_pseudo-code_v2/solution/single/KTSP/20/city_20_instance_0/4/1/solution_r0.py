import math
import random

# Coordinates of cities including the depot
cities = [
    (8, 11),   # Depot city 0
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

def euclidean_distance(a, b):
    x1, y1 = cities[a]
    x2, y2 = cities[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def evaluate_tour(tour):
    total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_distance

def generate_initial_solution():
    tour = [0]  # Start and end at the depot city
    available_cities = list(range(1, len(cities)))
    selected_cities = random.sample(available_cities, 3)
    tour.extend(selected_cities)
    tour.append(0)  # Finish at the depot city
    return tour

def local_search(tour):
    best_tour = tour[:]
    best_cost = evaluate_tour(best_tour)
    for i in range(1, len(tour) - 2):
        for j in range(i+1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = evaluate_tour(new_tour)
            if new_cost < best_cost:
                best_tour = new_tour[:]
                best_cost = new_cost
    return best_tour

def variable_neighborhood_search(max_iter=1000):
    current_tour = generate_initial_solution()
    current_cost = evaluate_tour(current_tour)
    for _ in range(max_iter):
        candidate_tour = generate_initial_solution()
        improved_tour = local_search(candidate_tour)
        improved_cost = evaluate_tour(improved_tour)
        if improved_cost < current_cost:
            current_tour = improved_tour[:]
            current_cost = improved_cost
    return current_tour, current_cost

best_tour, best_cost = variable_neighborhood_search()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")