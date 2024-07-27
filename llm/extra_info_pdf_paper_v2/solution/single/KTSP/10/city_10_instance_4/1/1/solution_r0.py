import random
import math
from itertools import permutations

# City coordinates
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
    5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate an initial random tour including the depot and exactly 7 other cities
def generate_initial_tour():
    tour = random.sample(list(cities.keys())[1:], 7)  # Exclude depot initially, sample 7 cities
    tour = [0] + tour + [0]  # Add depot to the start and end of the tour
    return tour

# Calculate the total travel cost of the tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Perform a 2-opt swap on the tour
def two_opt_swap(tour, i, k):
    return tour[:i] + tour[i:k+1][::-1] + tour[k+1:]

# Apply local search to improve the tour
def local_search(tour):
    best_cost = tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if j - i == 1: continue  # Avoid reversing a single element
                new_tour = two_opt_swap(tour, i, j)
                new_cost = tour_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improved = True
        if not improved:
            break
    return tour

# Main function to solve the problem
def solve_k_tsp():
    best_tour = generate_initial_tour()
    best_cost = tour_cost(best_tour)
    for _ in range(100):  # Perform 100 iterations to find a good solution
        tour = generate_initial_tour()
        improved_tour = local_search(tour)
        cost = tour_cost(improved_tour)
        if cost < best_cost:
            best_tour = improved_tour
            best_cost = cost
    return best_tour, best_cost

# Solve the problem and print the solution
final_tour, final_cost = solve_k_tsp()
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")