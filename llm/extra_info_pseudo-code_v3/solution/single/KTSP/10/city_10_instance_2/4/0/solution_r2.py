import numpy as np
import random

def calculate_distance(coords1, coords2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)

def generate_initial_tour(num_cities, k):
    """Generates a random tour of k cities starting and ending at the depot."""
    tour = list(range(1, num_cities))
    random.shuffle(tour)
    tour = tour[:k-1]
    tour = [0] + tour + [0] # start and end at the depot
    return tour

def tour_cost(tour, distance_matrix):
    """Calculate the cost of a given tour based on the distance matrix."""
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

def find_best_neighbor(tour, distance_matrix):
    """Find the best neighbor by trying all 2-opt swaps."""
    n = len(tour)
    best_cost = tour_cost(tour, distance_matrix)
    best_tour = tour[:]
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            if j - i == 1: continue # Skip adjacent boundaries (no effect)
            new_tour = tour[:]
            new_tour[i:j+1] = reversed(new_tour[i:j+1])
            new_cost = tour_cost(new_tour, distance_matrix)
            if new_cost < best_cost:
                best_cost = new_cost
                best_tour = new_tour
    return best_tour

def gvns(cities_coordinates, k, max_iterations=100):
    num_cities = len(cities_coordinates)
    # Creating distance matrix
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i][j] = calculate_distance(cities_coordinates[i], cities_coordinates[j])

    # Initialize the solution
    best_tour = generate_initial_tour(num_cities, k)
    best_cost = tour_cost(best_tour, distance_matrix)

    for _ in range(max_iterations):
        # Generate new initial tour
        new_tour = generate_initial_tour(num_cities, k)
        new_tour = find_best_neighbor(new_tour, distance_matrix)
        new_cost = tour_cost(new_tour, distance_matrix)

        # Apply local search to find local optimum
        local_optimal_tour = find_best_neighbor(new_tour, distance_matrix)
        local_optimal_cost = tour_cost(local_optimal_tour, distance_matrix)

        if local_optimal_cost < best_cost:
            best_tour, best_cost = local_optimal_tour, local_optimal_cost

    return best_tour, best_cost

# Defining the cities and their coordinates
cities_coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
    8: (49, 29), 9: (13, 17)
}

# Settings for the TSP
k = 6  # Total cities to visit including the depot

# Perform the General Variable Neighborhood Search
tour_result, cost_result = gvns(cities_coordinates, k)

print("Tour:", tour_result)
print("Total travel cost:", cost_result)