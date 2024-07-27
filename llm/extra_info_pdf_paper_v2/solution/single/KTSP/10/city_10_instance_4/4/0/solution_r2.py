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

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Calculate the total travel cost of the tour
def total_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Execute variable neighborhood descent for optimization
def variable_neighborhood_descent(initial_tour):
    best_tour = initial_tour[:]
    best_cost = total_tour_cost(best_tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best_tour) - 2):
            for j in range(i + 1, len(best_tour) - 1):
                new_tour = best_tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]  # Swap cities
                new_cost = total_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour[:]
                    improved = True
    return best_tour

# Randomly select initial cities, making sure to include the depot
def select_initial_cities():
    return [0] + random.sample(range(1, 10), 7)

# Main k-TSP solving using GVNS
def k_tsp_gvns():
    best_tour = None
    best_cost = float('inf')
    for _ in range(100):
        selected_cities = select_initial_cities()
        initial_tour = selected_cities + [0]  # Start and end at the depot
        refined_tour = variable_neighborhood_descent(initial_tour)
        tour_cost = total_tour_cost(refined_tour)
        if tour_cost < best_cost:
            best_cost = tour_cost
            best_tour = refined_tour
    return best_tour, best_cost

# Execute the function and print the results
tour, cost = k_tsp_gvns()
print("Tour:", tour)
print("Total travel cost:", cost)