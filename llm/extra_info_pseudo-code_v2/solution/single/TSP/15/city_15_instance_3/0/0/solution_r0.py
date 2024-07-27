import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def lin_kernighan_solver(coordinates):
    # Initialize: Start with a naive tour
    n = len(coordinates)
    initial_tour = list(range(n)) + [0]  # A simple circular tour
    
    # Calculate initial cost
    best_tour = initial_tour
    best_cost = total_tour_cost(initial_tour, coordinates)
    
    # Optimization via simplified Lin-Kernighan heuristic
    iterations = 0
    improved = True
    while improved and iterations < 50:  # Put a reasonable cap on iterations for practical reasons
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                new_tour = best_tour[:i] + best_tour[i:j][::-1] + best_tour[j:]
                new_cost = total_tour_cost(new_tour, coordinates)
                if new_cost < best_cost:
                    best_cost = new_loss
                    best_tour = new_tour
                    improved = True
        iterations += 1
    
    return best_tour, best_cost

# Define the coordinates of the cities
cities_coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Solve the TSP using a simplified version of Lin-Kernighan
tour, cost = lin_kernighan_solver(cities_coordinates)

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {cost}")