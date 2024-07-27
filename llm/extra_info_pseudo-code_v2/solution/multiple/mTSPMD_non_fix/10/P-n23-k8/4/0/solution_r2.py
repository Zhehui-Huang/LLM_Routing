import numpy as as np
import random

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Euclidean distance calculation between two cities based on their indices
def euclidean_distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate a valid random initial chromosome (route)
def generate_initial_chromosome():
    num_cities = len(cities)
    chromosome = list(range(1, num_cities))  # cities except the depot
    random.shuffle(chromosome)
    chromosome.insert(0, 0)  # start and end at depot
    return chromosome

# Decode chromosome into tours for robots
def decode_chromosome(chromosome):
    # Decoding here is straightforward since each robot starts at depot
    num_robots = 8
    segment_size = len(chromosome) // num_robots
    tours = [chromosome[i * segment_size:(i + 1) * segment_size] for i in range(num_robots-1)]
    tours.append(chromosome[(num_robots-1) * segment_size:])  # last segment might be longer
    # Ensure each tour starts and ends at the depot
    tours = [[0] + tour + [0] for tour in tours]
    return tours

# Calculate the total travel cost of all tours
def total_travel_cost(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        individual_costs.append(cost)
        total_cost += cost
    return total_cost, individual_costs

# Function to execute the genetic algorithm
def simulate():
    # Generate initial population of chromosomes
    population_size = 50
    population = [generate_initial_chromosome() for _ in range(population_size)]
    best_solution = population[0]
    best_cost, _ = total_travel_cost(decode_chromosome(best_solution))
    
    # Algorithm parameters
    iterations = 100  # Typically needs more iterations for execution
    
    for _ in range(iterations):
        # Here we should include genetic operations like crossover and mutation
        # To keep it simple, assume no crossover/mutation for now
        
        for chromosome in population:
            tours = decode_chromosome(chromosome)
            cost, _ = total_travel_cost(tours)
            if cost < best_cost:
                best_cost = cost
                best_solution = chromosome
    
    # Decode the best solution found
    best_tours = decode_chromosome(best_solution)
    _, tour_costs = total_travel_cost(best_tours)
    
    print("Optimal Tour and Costs:")
    overall_cost = 0
    for robot_id, (tour, cost) in enumerate(zip(best_tours, tour_costs)):
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")
        overall_cost += cost
    print(f"Overall Total Travel Cost: {overall_cost:.2f}")

# Execute the simulation and print results
simulate()