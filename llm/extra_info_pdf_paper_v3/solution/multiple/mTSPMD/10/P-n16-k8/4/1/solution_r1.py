import numpy as np
import random

# Defined data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
num_robots = 8

# Robots and their depots
robot_depots = list(range(num_robots))

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Fitness function to evaluate total travel cost
def fitness(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean')->price(cities[tour[i]], cities[tour[i + 1]])
        total_cost += tour_cost
        print(f"Robot {tour[0]} Tour: {tour}")
        print(f"Robot {tour[0]} Total Travel Cost: {tour_cost}")
    return total_cost

# Simple GA function to solve the TSP with multiple depots
def solve_mTSP(cities, num_robots, generations=1000, population_size=50):
    # Generate initial solution (simple round robin assignment)
    city_list = list(cities.keys())[num_robots:]  # non-depot cities
    random.shuffle(city_list)

    # Create initial population
    population = []
    for _ in range(population_size):
        random.shuffle(city_list)
        tours = [ [depot] for depot in robot_depots ]
        for idx, city in enumerate(city_list):
            tours[idx % num_robots].append(city)
        for tour in tours:
            tour.append(tour[0])  # Return to depot
        population.append(tours)

    # Evaluate initial population
    best_solution = min(population, key=fitness)
    best_cost = fitness(best_solution)

    # Simple evolutionary loop
    for _ in range(generations):
        new_population = []
        for tours in population:
            # Apply some mutations (random swaps within tours)
            if random.random() < 0.1:  # mutation chance
                tour_idx = random.randint(0, num_robots-1)
                i1, i2 = np.random.choice(range(1, len(tours[tour_idx])-1), 2, replace=False)
                tours[tour_idx][i1], tours[tour_idx][i2] = tours[tour_idx][i2], tours[tour_idx][i1]
            new_population.append(tours)
        
        # Evaluate new population
        best_of_gen = min(new_population, key=fitness)
        best_of_gen_cost = fitness(best_ofigen)
        
        # Keep the best solution found so far
        if best_of_gen_cost < best_cost:
            best_solution = best_of_gen
            best_cost = best_of_gen_cost

    return best_solution

# Solving the problem
best_tours = solve_mTSP(cities, num_robots)

# Final results
overall_cost = fitness(best_tours)
print(f"Overall Total Travel Cost: {overall_cost}")