import random
import itertools
import math

# Define the city coordinates
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), 
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((coordinates[c1][0] - coordinates[c2][0]) ** 2 + (coordinates[c1][1] - coordinates[c2][1]) ** 2)

# Compute the total distance for the tour
def calculate_total_distance(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate a random initial solution
def generate_initial_solution():
    cities = random.sample(range(1, 20), 3)
    tour = [0] + cities + [0]
    return tour

# Local search to optimize the tour using 2-opt swaps
def local_search(tour):
    best_distance = calculate_total_distance(tour)
    best_tour = tour[:]
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour) - 3):
            for j in range(i+2, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j] = reversed(tour[i:j])
                new_distance = calculate_total_distance(new_tour)
                if new_distance < best_distance:
                    best_tour = new_tour[:]
                    best_distance = new_distance
                    improved = True
        tour = best_tour
    return tour

# Simulate shake for diversification
def shake(tour):
    idx = list(range(1, len(tour) - 1))
    i1, i2 = random.sample(idx, 2)
    tour[i1], tour[i2] = tour[i2], tour[i1]
    return tour

# Implement the GVNS algorithm
def gvns(itermax=100, kmax=5):
    best_solution = generate_initial_solution()
    best_cost = calculate_total_distance(best_solution)
    
    for _ in range(itermax):
        current_solution = shake(best_solution[:])
        current_solution = local_search(current_solution)
        current_cost = calculate_total_distance(current_solution)
        
        if current_cost < best_cost:
            best_solution = current_solution[:]
            best_cost = current_cost
    
    return best_solution, best_cost

# Run the GVNS algorithm
final_tour, final_cost = gvns()
print("Tour:", final_tour)
print("Total travel cost:", round(final_cost, 2))