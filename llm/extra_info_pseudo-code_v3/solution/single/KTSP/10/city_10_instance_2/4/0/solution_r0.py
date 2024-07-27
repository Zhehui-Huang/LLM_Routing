import numpy as np
import random

# Environment information
cities_coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81),
    4: (41, 54), 5: (31, 35), 6: (23, 95), 7: (20, 56),
    8: (49, 29), 9: (13, 17)
}

# Calculate a basic Euclidean distance matrix
def compute_distance_matrix(cities):
    num_cities = len(cities)
    D = np.zeros((num_cities, num_cities))
    
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                pi, pj = cities[i], cities[j]
                D[i][j] = np.sqrt((pi[0] - pj[0])**2 + (pi[1] - pj[1])**2)
    return D

# Generate an initial solution with k cities including the depot
def generate_initial_solution(cities, k):
    chosen_cities = [0] + random.sample(list(cities.keys())[1:], k-1)
    return chosen_cities

# Calculate the tour distance
def evaluate_tour(tour, D):
    return sum(D[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Neighborhood operation: remove-add a city
def neighborhood_select_replace(tour, candidate_cities, D):
    best_tour = tour[:]
    best_cost = evaluate_tour(tour + [0], D)
    
    for current in tour[1:]:
        for candidate in candidate_cities:
            if candidate not in tour:
                new_tour = tour[:]
                new_tour.remove(current)
                new_tour.append(candidate)
                cost = evaluate_tour(new_tour + [0], D)
                if cost < best_cost:
                    best_tour, best_cost = new_tour, cost
    return best_tour

# Variable Neighborhood Descent
def vnd(tour, candidate_cities, D):
    current_tour = tour[:]
    improved = True
    while improved:
        new_tour = neighborhood_select_replace(current_tour, candidate_cities, D)
        if new_tour != current_tour:
            current_tour = new_tour
        else:
    improved = False
    return current_tour

# General Variable Neighborhood Search Algorithm
def gvns(V, k, D, Nrst=50):
    best_tour = generate_initial_solution(V, k)
    best_cost = evaluate_tour(best_tour + [0], D)
    
    for _ in range(Nrst):
        current_tour = generate_initial_solution(V, k)
        current_tour = vnd(current_tour, V, D)
        current_cost = evaluate_tour(current_tour + [0], D)

        if current_cost < best_cost:
            best_tour, best_cost = current_tour, current_cost
            
    return best_tour + [0], best_cost

# Main execution
city_count = 6  # depot plus 5 other cities as per problem statement
distance_matrix = compute_distance_matrix(cities_coordinates)
tour, cost = gvns(cities_coordinates, city_count, distance_matrix)

print("Tour:", tour)
print("Total travel cost:", cost)