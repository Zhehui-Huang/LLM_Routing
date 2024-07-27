import numpy as np
import random

# City Coordinates
cities = [
    (79, 15), # Depot city 0
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

# Distance calculation function
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate initial feasible solution
def generate_initial_solution():
    available_cities = list(range(1, len(cities)))  # All cities except the depot
    selected_cities = random.sample(available_cities, 7)  # Select 7 cities randomly as we include the depot twice
    tour = [0] + selected_cities + [0]
    return tour

# Calculate total cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_search(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Local search by swapping two cities in the tour
def local_search(tour):
    best_tour = tour[:]
    best_cost = calculate_tour_cost(tour)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = calculate_tour_cost(new_tour)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour
    return best_tour

# Shake function to escape local minima
def shake(tour, k):
    internal_cities = tour[1:-1]
    random.shuffle(internal_cities)
    new_tour = [tour[0]] + internal_cities[:k-1] + [tour[0]]
    return new_tour

# Main function to run the GVNS
def run_gvns(iterations):
    best_tour = generate_initial_solution()
    best_cost = calculate_tour_cost(best_tour)
    
    for _ in range(iterations):
        current_tour = shake(best_tour, 7)
        current_tour = local_search(current_tour)
        current_cost = calculate_tour_cost(current_tour)
        
        if current_cost < best_cost:
            best_tour, best_cost = current_tour, current_cost
    
    return best_tour, best_cost

# Run the solution
best_tour, best_cost = run_gvns(1000)  # Use 1000 iterations for the search

# Output the tour and the total travel cost
print("Tour:", best_tour)
print("Total travel cost:", best_cost)