import random
import math

# Coordinates of the cities including the depot
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_tour_length(tour):
    """Calculate the total tour length."""
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_initial_tour():
    """Find an initial feasible tour randomly selecting cities."""
    selected_cities = random.sample(list(coordinates.keys())[1:], 9)
    selected_cities = [0] + selected_cities + [0]
    return selected_cities

def perform_local_search(tour):
    """Optimize the tour using local search by swapping."""
    improved = True
    while improved:
        improved = False
        best_length = total_tour_length(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                if j - i == 1: continue  # Skip adjacent cities
                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
                new_length = total_tour_length(new_tour)
                if new_length < best_length:
                    tour = new_tour
                    best_length = new_length
                    improved = True
    return tour

def solve_k_tsp():
    best_tour = find_initial_tour()
    best_length = total_tour_length(best_tour)
    
    # Perform the local search
    best_tour = perform_local_search(best_tour)
    best_length = total_tour_length(best_tour)

    # Output the tour and total travel cost
    return best_tour, best_length

# Solve the k-TSP
tour, total_cost = solve_k_tsp()

# Output the result
print('Tour:', tour)
print('Total travel cost:', total_cost)