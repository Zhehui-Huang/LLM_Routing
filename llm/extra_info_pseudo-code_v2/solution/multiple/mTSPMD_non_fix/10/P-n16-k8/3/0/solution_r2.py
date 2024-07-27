import numpy as np
import random
import math

# Coordinates of cities and depots
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

num_robots = 8
depot = 0  # All robots start at depot city 0

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((coords[p1][0] - coords[p2][0]) ** 2 + (coords[p1][1] - coords[p2][1]) ** 2)

# Initialize the distance matrix
distance_matrix = [[euclidean_distance(i, j) for j in range(len(coords))] for i in range(len(coords))]

# Generate an initial feasible solution
def generate_initial_solution():
    cities = list(range(1, len(coords)))  # exclude the depot
    random.shuffle(cities)
    parts = len(cities) // num_robots
    solutions = [[depot] for _ in range(num_robots)]
    for i in range(num_robots):
        solutions[i].extend(cities[i*parts:(i+1)*parts if i < num_robots - 1 else None])
        solutions[i].append(depot)  # loop back to the starting depot after finishing the tour
    return solutions

# Calculate the cost of a solution
def calculate_costs(tours):
    total_cost = 0
    detailed_costs = []
    for tour in tours:
        tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        detailed_costs.append(tour_cost)
        total_cost += tour_cost
    return detailed_costs, total_cost

# Define the genetic algorithm process
def genetic_algorithm(iterations=1000, population_size=100, mutate_chance=0.1):
    population = [generate_initial_solution() for _ in range(population_size)]
    best_solution = None
    best_cost = float('inf')

    for _ in range(iterations):
        # Assess fitness
        ranked_solutions = sorted([(tour, calculate_costs(tour)[1]) for tour in population], key=lambda x: x[1])
        if ranked_solutions[0][1] < best_cost:
            best_cost = ranked_solutions[0][1]
            best_solution = ranked_solutions[0][0]

        # Select survivors
        survivors = [tour for tour, cost in ranked_solutions[:int(0.2 * len(ranked_solutions))]]
        
        # Repopulate
        new_population = survivors[:]
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(survivors, 2)
            child1, child2 = crossover(parent1, parent2)
            if random.random() < mutate_chance:
                mutate(child1)
                mutate(child2)
            new_population.extend([child1, child2])

        population = new_population[:population_size]

    return best_solution, best_cost

# Let's run the genetic algorithm
best_route, best_route_cost = genetic_algorithm()

# Deduce detailed cost for the final solution
individual_costs, total_cost = calculate_costs(best_route)

# Output the results
for i, route in enumerate(best_route):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {individual_costs[i]}")

print(f"\nOverall Total Travel Cost: {total_cost}")