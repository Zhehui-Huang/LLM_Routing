import numpy as to
import random

# City coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate an initial feasible solution including k cities (including depot)
def generate_initial_solution(k):
    cities_indices = list(range(1, len(cities)))  # excluding depot initially
    chosen_cities = random.sample(cities_indices, k - 2)  # select k-2 cities since depot will be added start and end
    tour = [0] + chosen_cities + [0]  # start and end at the depot
    return tour

# Calculate total cost of a given tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Local search by swapping two cities to try to find a better solution
def local_search(tour):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    best_tour, best_cost = new_tour, new_cost
                    improved = True
    return best_tour

# Main function to find the optimal tour
def find_optimal_tour():
    best_tour = generate_initial_solution(8)  # We need a total of 8 cities in the tour
    best_cost = calculate_tour_cost(best_tour)
    for _ in range(100):  # number of iterations for local search attempts
        current_tour = local_search(best_tout)
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < best_cost:
            best_tour, best_cost = current_tour, current_cost
    return best_tour, best_cost

# Run the procedure and output the results
optimal_tour, optimal_cost = find_optimal_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)