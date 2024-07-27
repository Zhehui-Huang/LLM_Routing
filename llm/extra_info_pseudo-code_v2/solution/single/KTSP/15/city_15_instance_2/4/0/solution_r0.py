import math
import random

# City coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30),
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def calculate_total_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

def initial_tour():
    tour = [0]  # start with depot city
    while len(tour) < 8:
        new_city = random.choice([i for i in range(1, len(cities)) if i not in tour])
        tour.append(new_city)
    tour.append(0)  # end at the depot city
    return tour

def shake(tour):
    base_tour = tour[1:-1]
    random.shuffle(base_tour)
    return [0] + base_tour + [0]

def local_search_exchange(tour):
    for i in range(1, len(tour) - 1):
        for j in range(1, len(cities)):
            if j not in tour:
                new_tour = tour[:i] + [j] + tour[i+1:]
                new_tour[-1] = 0
                if calculate_total_cost(new_tour) < calculate_total_cost(tour):
                    return new_tour
    return tour

def local_search_swap(tour):
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            if calculate_total_cost(new_tour) < calculate_total_cost(tour):
                return new_tour
    return tour

def vnd(tour):
    improved = True
    while improved:
        new_tour = local_search_exchange(tour)
        if new_tour == tour:
            new_tour = local_search_swap(tour)
            if new_tour == tour:
                improved = False
            else:
                tour = new_tour
        else:
            tour = new_tour
    return tour

# GVNS
random.seed(0)  # For repeatability
best_tour = None
best_cost = float('inf')
itermax = 10

for _ in range(itermax):
    tour = initial_tour()
    for _ in range(5):  # pmax
        tour_prime = shake(tour)
        tour_prime_prime = vnd(tour_prime)
        cost = calculate_total_cost(tour_prime_prime)
        if cost < best_cost:
            best_tour = tour_prime_prime
            best_cost = cost

# Outputs
print("Tour:", best_tour)
print(f"Total travel cost: {best_cost:.2f}")