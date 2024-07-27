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
        for j in range(i, num_cities):
            pi, pj = cities[i], cities[j]
            dist = np.sqrt((pi[0] - pj[0])**2 + (pi[1] - pj[1])**2)
            D[i][j] = D[j][i] = dist
    return D

# Generate an initial solution with k cities including the depot
def generate_initial_solution(cities, k):
    chosen_cities = [0] + random.sample(list(cities.keys())[1:], k-1)
    return chosen_cities

# Calculate the tour distance
def evaluate_tour(tour, D):
    tour_cost = sum(D[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    tour_cost += D[tour[-1]][tour[0]]  # to return to the depot
    return tour_cost

# Neighborhood operations: Swapping two cities
def neighborhood_swap(tour, D):
    best_tour = tour[:]
    best_cost = evaluate_tour(tour, D)
    
    for i in range(1, len(tour)-1):
        for j in range(i+1, len(tour)):
            new_tour = tour[:]
            new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
            new_cost = evaluate_tour(new_tour, D)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour, new_cost
    return best_tour

# Variable Neighborhood Descent (VND)
def vnd(tour, D):
    current_tour = tour[:]
    improving = True
    while improving:
        new_tour = neighborhood_swap(current_tour, D)
        if new_tour != current_tour:
            current_tour = new_tour
        else:
            improving = False
    return current_tour

# General Variable Neighborhood Search (GVNS)
def gvns(V, k, D, Nrst=100):
    best_tour = generate_initial_solution(V, k)
    best_tour = vnd(best_tour, D) + [0]
    best_cost = evaluate_tour(best_tour, D)
    
    for _ in range(Nrst):
        current_tour = generate_initial_solution(V, k)
        current_tour = vnd(current_tour, D) + [0]
        current_cost = evaluate_tour(current_tour, D)
        if current_cost < best_cost:
            best_tour, best_cost = current_tour, current_cost
            
    return best_tour, best_cost

# Main execution
city_count = 6  # depot plus 5 other cities as per problem statement
distance_matrix = compute_distance_matrix(cities_coordinates)
tour, cost = gvns(cities_coordinates, city_count, distance.EmptyArray)

print("Tour:", tour)
print("Total travel cost:", cost)