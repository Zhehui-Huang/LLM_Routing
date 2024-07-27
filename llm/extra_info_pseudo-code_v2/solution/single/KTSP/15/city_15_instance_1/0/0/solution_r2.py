import random
import math

# Define the cities and their coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def generate_initial_solution(k):
    city_indices = list(cities.keys())
    random.shuffle(city_indices)
    tour = [0] + random.sample(city_indices[1:], k-2) + [0]  # making sure to start and end at the depot
    return tour

def shake(tour, k):
    interior = tour[1:-1]
    random.shuffle(interior)
    return [0] + interior + [0]

def local_search(tour):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour)
    made_improvement = True

    while made_improvement:
        made_improvement = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour) - 1):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour[:]
                    made_improvement = True

    return best_tour

def GVNS(k, max_iter=100, max_no_improv=10):
    best_tour = generate_initial_solution(k)
    best_cost = calculate_tour_cost(best_tour)
    no_improvement = 0

    while no_improvement < max_no_improv:
        current_tour = shake(best_tour, k)
        current_tour = local_search(current_tour)
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < best_cost:
            best_tour, best_cost = current_tour, current_cost
            no_improvement = 0
        else:
            no_improvement += 1

    return best_tour, best_cost

# Solve for a tour choosing exactly 6 cities
best_tour, best_cost = GVNS(6)
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))