import random
import numpy as np

# Locations of cities including the depot city
locations = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((locations[city1][0] - locations[city2][0])**2 + (locations[city1][1] - locations[city2][1])**2)

# Generate an initial solution: start at depot, select 4 random other cities, and return to depot
def generate_initial_solution():
    cities = list(range(1, len(locations)))  # All cities except the depot
    random.shuffle(cities)
    selected_cities = cities[:4]
    tour = [0] + selected_cities + [0]
    return tour

# Calculate total travel cost of a tour
def tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Shake function to explore neighborhood
def shake(tour):
    new_tour = tour[1:-1]  # exclude the depot for swapping
    idx1, idx2 = random.sample(range(len(new_tour)), 2)
    new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]
    return [0] + new_tour + [0]

# Local search to find a better neighbor
def local_search(tour):
    best_tour = tour[:]
    best_cost = tour_cost(tour)
    for i in range(1, len(tour) - 2):
        for j in range(i + 1, len(tour) - 1):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = tour_cost(new_tour)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour[:]
    return best_tour

# Variable neighborhood descent
def VND(tour):
    current_tour = tour[:]
    improved = True
    while improved:
        new_tour = local_search(current_tour)
        if tour_cost(new_tour) < tour_cost(current_tour):
            current_tour = new_tour[:]
        else:
            improved = False
    return current_tour

# Implementing the GVNS
def GVNS(max_iter=100):
    best_tour = generate_initial_solution()
    best_cost = tour_cost(best_tour)
    
    for _ in range(max_iter):
        current_tour = shake(best_tour)
        current_tour = VND(current_tour)
        current_cost = tour_cost(current_tour)
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    
    return best_tour, best_cost

# Execute the algorithm
final_tour, final_cost = GVNS(200)
print(f"Tour: {final_tour}")
print(f"Total travel cost: {final_cost:.2f}")