import numpy as np
import random

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Calculate Euclidean distance
def distance(idx1, idx2):
    return np.sqrt((cities[idx1][0] - cities[idx2][0]) ** 2 + (cities[idx1][1] - cities[idx2][1]) ** 2)

# Generate a random solution of tours with the robots starting at city 0
def generate_solution():
    rest_cities = list(range(1, len(cities)))
    random.shuffle(rest_cities)
    # Even distribution of the cities among the robots
    robot_tours = [[] for _ in range(num_robots)]
    tour_lengths = [1] * num_robots  # Start with initial city, the depot
    
    robot = 0
    for city in rest_cities:
        robot_tours[robot].append(city)
        robot = (robot + 1) % num_robots

    # Start and end at the depot
    for tour in robot_tours:
        tour.insert(0, 0)  # starting at the depot
    return robot_tours

# Total cost of tours
def total_cost(tours):
    total = 0
    results = []
    for tour in tours:
        tour_cost = 0
        for i in range(1, len(tour)):
            tour_cost += distance(tour[i-1], tour[i])
        # travel back to depot from the last city in the tour
        results.append((tour, tour_cost))
        total += tour_cost
    return results, total

# Simulation parameters
num_robots = 8
population_size = 30
generations = 100
mutation_rate = 0.1
crossover_rate = 0.8

# Generate random initial population of tours
population = [generate_solution() for _ in range(population_size)]
best_solution = None
lowest_cost = float('inf')

# Run GA over generations
for _ in range(generations):
    # Evaluate population
    evaluated = [total_cost(individual) for individual in population]
    evaluated.sort(key=lambda x: x[1])
    
    if evaluated[0][1] < lowest_cost:
        lowest_cost = evaluated[0][1]
        best_solution = evaluated[0][0]

    # Selection -- elitism
    selected = [x[0] for x in evaluated[:population_size//2]]
    
    # Crossover and mutation -- crossover and simple mutation for education purposes
    new_population = selected[:]
    while len(new_temperature) < population_size:
        # Mutation: simple swap mutation for demonstration
        if random.random() < mutation_rate:
            tour_copy = random.choice(selected).copy()
            for tour in tour_copy:
                if len(tour) > 2:  # Ensure it's possible to swap
                    idx1, idx2 = random.sample(range(1, len(tour)), 2)
                    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]
            new_population.append(tour_copy)

    population = new_population

# Final solution
best_routes, best_total_cost = total_cost(best_solution)

# Output
for idx, (route, cost) in enumerate(best_routes):
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {best_total_cost}")