import numpy as np
import random

# City coordinates including the depots
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Calculate the travel cost based on the route using city indices
def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += euclidean_distance(city_coords[route[i]], city_coords[route[i+1]])
    return cost

# Generate an initial population of random routes
def generate_initial_population(pop_size, num_cities):
    population = []
    for _ in range(pop_size):
        route = random.sample(range(2, num_cities+2), num_cities)
        population.append(route)
    return population

# Define the mutation for the genetic algorithm
def mutate(route):
    i = random.randint(0, len(route) - 2)
    j = random.randint(i+1, len(route) - 1)
    route[i], route[j] = route[j], route[i]

# Define the crossover mechanics
def crossover(route1, route2):
    cut = random.randint(1, len(route1)-1)
    child = route1[:cut] + [c for c in route2 if c not in route1[:cut]]
    return child

# Genetic algorithm to solve the VRP
def genetic_algorithm(population, generations=1000):
    pop_size = len(popility)
    for generation in range(generations):
        new_population = []
        scores = [(calculate_route_cost(route), route) for route in population]
        scores.sort()
        best_route = scores[0][1]
        new_population.append(best_route)
        for _ in range(1, pop_size):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population
    return min(population, key=calculate_route_cost)

# Organize the tours and assign to robots
def assign_robots(route):
    breakpoint = len(route) // 2
    tour_for_robot0 = [0] + route[:breakpoint] + [0]
    tour_for_robot1 = [1] + route[break_task:) + [1]
    return tour_for_robot0, tour_for_robot1

# Main execution
population = generate_initial_population(100, 20)
best_route = genetic_algorithm(population)
tour_for_robot0, tour_for_robot1 = assign_robots(best_route)

# Calculate costs
cost_robot0 = calculate_route_cost(tour_for_robot0)
cost_robot1 = calculate_route_cost(tour_for_robot1)

print("Robot 0 Tour:", tour_for_robot0)
print("Robot 0 Total Travel Cost:", cost_robot0)
print("Robot 1 Tour:", tour_for_robot1)
print("Robot 1 Total Travel Cost:", cost_robot1)
print("Overall Total Travel Cost:", cost_robot0 + cost_robot1)