import math
import random

# Define city coordinates (index 0 is the depot)
cities = [
    (79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)
]

# Function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Initialize the current best tour and its cost
def initial_tour():
    # Starting at the depot, pick 7 additional unique cities randomly, then return to the depot
    selected_cities = [0] + random.sample(range(1, 10), 7) + [0]
    return selected_cities

def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Local search to improve a given tour
def local_search(tour):
    min_cost = calculate_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # skip adjacent cities
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < min_cost:
                    tour = new_tour
                    min_cost = new_cost
                    improved = True
    return tour, min_cost

# General Variable Neighborhood Search
def GVNS(max_iterations):
    best_tour = initial_tour()
    best_cost = calculate_tour_cost(best_tour)
    for _ in range(max_iterations):
        new_tour = initial_tour()
        new_tour, new_cost = local_search(new_tour)
        if new_cost < best_cost:
            best_tour = new_tour
            best_cost = new_cost
    return best_tour, best_cost

# Let's run the metaheuristic for a suitable number of iterations
final_tour, final_cost = GVNS(1000)

# Output
print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))