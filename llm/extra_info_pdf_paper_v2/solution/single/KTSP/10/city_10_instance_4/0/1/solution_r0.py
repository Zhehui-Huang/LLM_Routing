import math
import random
from itertools import permutations

# City coordinates
cities = {
    0: (79, 15),  # depot city
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

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    coord1, coord2 = cities[city1], cities[city2]
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

# Implement GVNS-based method to solve k-TSP
def k_tsp_gvns(cities, k):
    # Start with a random selection of k cities including the depot city 
    current_solution = [0] + random.sample(list(cities.keys())[1:], k-1)
    current_solution.append(0)  # Return back to the depot
    best_cost = calculate_tour_cost(current_solution)
    
    # Variable Neighborhood Descent (VND)
    for iteration in range(1000):
        new_solution = current_solution[:]
        # Shake: Swap two cities
        swap_indices = random.sample(range(1, k), 2)
        new_solution[swap_indices[0]], new_solution[swap_indices[1]] = new_solution[swap_indices[1]], new_solution[swap_indices[0]]
        new_solution[-1] = new_solution[0]
        
        # Calculate the cost
        new_cost = calculate_tour_cost(new_solution)
        if new_cost < best_cost:
            current_solution, best_cost = new_solution, new_cost
            
    return current_solution, best_cost

# Calculate total tour cost
def calculate_torsequence_distance(destination_sequence):
    return sum(distance(destination_sequence[i], destination_sequence[i+1]) for i in range(len(destination_sequence)-1))

# Solver execun_cost(distance_sequence):
    tour_cost=0
    for i in range(len(distance_sequence)-1):
        tour_cost += math.sqrt((cities[distance_sequence[i+1]][0]-cities[distance_sequence[i]][0])**2 + (cities[distance_sequence[i+1]][1]-cities[distance_sequence[i]][1])**2)
    return tour_cost

# Main execution
selected_k = 8  # including the depot city
best_tour, best_tour_cost = k_tsp_gvns(cities, selected_k)

print("Tour:", best_tour)
print("Total travel cost:", round(best_tour_cost, 2))