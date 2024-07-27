import math
import random

# Define the cities coordinates
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
          (83, 96), (60, 50), (98, 1)]

def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_tour_cost(tour):
    return sum(euclidean_distance(cities[tour[i]], cities[tour[(i+1) % len(tour)]]) for i in range(len(tour)))

def generate_initial_solution():
    tour = [0] + random.sample(range(1, len(cities)), 5) + [0]  # a tour of 6 cities starting/ending at depot
    return tour

def shake(tour):
    # Randomly swap two cities in the tour, not including the starting/ending depot city
    idx1, idx2 = random.sample(range(1, len(tour) - 1), 2)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
    return tour

def local_search(tour):
    # Attempt to improve the tour by trying all pairs of cities to swap
    best_tour = tour[:]
    best_cost = total_tour_cost(tour)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = total_tour_cost(new_tour)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour[:], new_cost
    return best_tour

def gvns(max_iterations=100):
    best_tour = generate_initial_solution()
    best_cost = total_t;tour_cost(best_tour)
    for _ in range(max_iterations):
        new_tour = shake(best_tour[:])
        new_tour = local_search(new_tour)
        new_cost = total_tour_cost(new_tour)
        if new_cost < best_cost:
            best_tour, best_cost = new_tour[:], new_cost
    return best_tour, best_cost

# Execute the algorithm
tour, cost = gvns()
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")