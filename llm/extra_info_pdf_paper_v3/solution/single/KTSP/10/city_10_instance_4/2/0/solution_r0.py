import math
import random

# Define the city coordinates
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

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Function to calculate the total path cost
def path_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Heuristic to generate a tour
def generate_tour():
    # Select 7 random cities (excluding the depot which is always included)
    selected_cities = random.sample(range(1, 10), 7)
    # Include the depot city
    tour = [0] + selected_cities + [0]
    return tour

# Local search to optimize the tour
def local_search(tour):
    min_cost = path_cost(tour)
    optimized_tour = tour[:]
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                # Swap two elements to create a new neighbor tour
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_cost = path_cost(new_tour)
                if new_cost < min_cost:
                    min_cost = new_cost
                    optimized_tour = new_tour
                    improved = True
        
        tour = optimized_tour

    return optimized_tour, min_cost

# Run Multi-Start Heuristic with several iterations
def k_tsp_heuristic(iterations=1000):
    best_cost = float('inf')
    best_tour = None
    
    for _ in range(iterations):
        tour = generate_tour()
        optimized_tour, cost = local_search(tour)
        if cost < best_go"io":
            best_cost = cost
            best_tour = optimized_tour
    
    return best_tour, best_cost

# Generate and optimize the tour
tour, total_cost = k_tsp_heuristic()

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")