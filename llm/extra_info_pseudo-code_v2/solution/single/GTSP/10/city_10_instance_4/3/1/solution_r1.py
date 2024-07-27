from math import sqrt
import random

# City positions
depot = (79, 15)
cities = [(79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), 
         (20, 99), (66, 62)]

# City groups
city_groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]  # groups consist of indices in the cities' order

# Calculate Euclidean distance
def distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate an initial tour by selecting one city from each group and adding the depot at the beginning and end
def initial_tour():
    tour_indices = [0]  # Starts at the depot
    for group in city_groups:
        chosen_index = random.choice(group)
        tour_indices.append(chosen_index)
    tour_indices.append(0)  # Ends at the depot
    return tour_indices

# Compute cost of the tour
def compute_total_cost(tour_indices):
    total_cost = 0
    locations = [depot] + [cities[i - 1] for i in tour_indices[1:-1]] + [depot]
    for i in range(len(locations) - 1):
        total_cost += distance(locations[i], locations[i + 1])
    return total_cost

# Find best tour
def find_best_tour(num_trials):
    best_tour_indices = None
    best_cost = float('inf')
    
    for _ in range(num_trials):
        tour_indices = initial_tour()
        cost = compute_total_cost(tour_indices)
        if cost < best_cost:
            best_tour_indices = tour_indices
            best_cost = cost
    
    return best_tour_indices, best_cost

# Run the function with a number of trials
num_trials = 5000
best_tour_indices, best_cost = find_best_tour(num_trials)

# Print the results
print("Tour:", best_tour_indices)
print("Total travel cost:", round(best_cost, 2))