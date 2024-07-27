import math
import random

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def variable_neighborhood_descent(initial_tour):
    best_tour = initial_tour.copy()
    best_cost = total_tour_cost(best_tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i+1, len(best_tour) - 1):
                new_tour = best_tour.copy()
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour
                    improved = True
    return best_tour

def select_initial_cities():
    return [0] + random.sample(range(1, 10), 7)

def k_tsp_gvns():
    best_tour = []
    best_cost = float('inf')

    for _ in range(100):  # GVNS iterations
        selected_cities = select_initial_cities()
        initial_tour = selected_cities + [selected_cities[0]]
        refined_tour = variable_neighborhood_descent(initial_tour)
        tour_cost = total_tour_cost(refined_tour)
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_tour = refined_tour
            
    return best_tour, best_cost

# Main computation
tour, cost = k_tsp_gvns()
result = {
    "Tour": tour,
    "Total travel cost": cost
}
result