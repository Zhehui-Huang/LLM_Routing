import math
import random

# City coordinates
cities = {
    0: (54, 87),  1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30),  6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance between two cities
def calc_distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate initial tour including exactly k cities with depot at start and finish
def generate_initial_tour(k):
    tour = random.sample(list(cities.keys()), k)
    if 0 not in tour:
        tour.pop()
        tour.insert(0, 0)
    tour.append(0)  # Return to the depot
    return tour

# Calculate the travel cost of the tour
def tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Local Search to optimize the tour
def local_search(tour):
    best_cost = tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # Skip consecutive cities
                new_tour = tour[:]
                new_tour[i:j] = reversed(tour[i:j])
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    tour, best_cost = new_tour, new_cost
                    improved = True
    return tour, best_cost

# General VNS
def vns(k, max_attempts=100):
    best_tour = generate_initial_tour(k)
    best_tour, best_cost = local_search(best_tour)
    attempt = 0
    while attempt < max_attempts:
        k_tour = generate_initial_tour(k)
        k_tour, k_cost = local_search(k_tour)
        if k_cost < best_cost:
            best_tour, best_cost = k_tour, k_cost
            attempt = 0
        else:
            attempt += 1
    return best_tour, best_cost

# Run VNS
final_tour, final_cost = vns(8)
print("Tour:", final_tour)
print(f"Total travel cost: {final_cost:.2f}")