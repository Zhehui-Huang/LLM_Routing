import math
import random

# Parameters
num_cities = len(cities)
antnum = 20
cyclenum = 100
init_trail = 1.0
alpha = 1
beta = 5
rho = 0.1

# Initialize pheromones and heuristic visibility
pheromone = initialize_pheromones(num_cities, init_trail)
visibility = initialize_visibility(num_cities)

# Main ACO
best_cost = float('inf')
best_tour = None

for cycle in range(cyclenum):
    all_tours = []
    all_costs = []

    for ant in range(antnum):
        # Start each robot from its respective depot
        if ant % 2 == 0:
            start_city = 0  # Robot 0 starts at depot 0
        else:
            start_city = 1  # Robot 1 starts at depot 1

        tour = [start_city]
        current_city = start_city
        allowed = list(set(range(num_cities)) - {current_city})

        while allowed:
            probabilities = transition_probabilities(current_city, allowed, pheromone, visibility, alpha, beta)
            next_city = select_next_city(probabilities)
            tour.append(next_city)
            allowed.remove(next_city)
            current_city = next_city

        tour.append(start_city)  # Complete the tour by returning to the depot

        # Calculate tour cost
        cost = calculate_tour_cost(tour)
        all_tours.append(tour)
        all_costs.append(cost)

        # Update pheromone trail
        for i in range(len(tour) - 1):
            a, b = tour[i], tour[i+1]
            pheromone[a][b] += 1 / cost
            pheromone[b][a] += 1 / cost

    # Evaporate pheromone
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone[i][j] *= (1 - rho)

    # Identify the best solution
    min_cost_index = all_costs.index(min(all_costs))
    if all_costs[min_cost_index] < best_cost:
        best_cost = all_costs[min_cost_index]
        best_tour = all_tours[min_cost_index]

# Output results
print("Best tour found:", best_tour)
print("Cost of the best tour:", best_cost)