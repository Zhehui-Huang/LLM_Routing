from itertools import permutations
import numpy as np
import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Calculate distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate distance matrix
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i, j] = distance(i, j)

# Initialize ACO parameters
num_ants = 40
num_iterations = 100
decay = 0.5
alpha = 1  # influence of pheromone
beta = 5   # influence of heuristic
initial_pheromone = 10 / n_cities

# Pheromone matrix
pheromones = np.ones((n_cities, n_cities)) * initial_pheromone

def aco_tsp():
    best_cost = float('inf')
    best_solution = []

    for iteration in range(num_iterations):
        solutions = []
        costs = []
        
        for _ in range(num_ants):
            # Each ant generates two tours starting from depots 0 and 1
            tour_0 = [0]
            tour_1 = [1]
            unvisited = set(cities.keys()) - {0, 1}
            
            for tour in [tour_0, tour_1]:
                while len(unvisited) > 1:
                    current = tour[-1]

                    # Calculate transition probabilities
                    transition_probs = []
                    for next_city in unvisited:
                        if next_city != tour[0]:  # avoid the depot itself in mid-tour
                            prob_numerator = (pheromones[current][next_city]**alpha) * ((1 / distance_matrix[current][next_city])**beta)
                            transition_probs.append((next_city, prob_numerator))
                    
                    total_prob = sum(prob for _, prob in transition_probs)
                    if total_prob == 0:
                        break  # no viable moves
                    probs = [prob/total_prob for _, prob in transition_probs]
                    next_city = np.random.choice([city for city, _ in transition_probs], p=probs)
                    
                    tour.append(next_city)
                    unvisited.remove(next_city)

                tour.append(tour[0])  # complete the tour by returning to the depot
            
            # Calculate cost of each robot's tour
            cost_0 = sum(distance_matrix[tour_0[i]][tour_0[i+1]] for i in range(len(tour_0)-1))
            cost_1 = sum(distance_matrix[tour_1[i]][tour_1[i+1]] for i in range(len(tour_1)-1))
            total_cost = cost_0 + cost_1

            if total_cost < best_cost:
                best_cost = total_cost
                best_solution = [tour_0, tour_1, best_cost, total_cost]
            
            solutions.append([tour_0, tour_1])
            costs.append(total_cost)

        # Update pheromones
        pheromones *= decay  # decay pheromones
        for cost, (solution_0, solution_1) in zip(costs, solutions):
            for tour in [solution_0, solution_1]:
                contribution = 1 / cost
                for i in range(len(tour) - 1):
                    pheromones[tour[i]][tour[i+1]] += contribution

    return best_solution

best_path = aco_tsp()

# Output
print("Robot 0 Tour:", best_path[0])
print("Robot 0 Total Travel Cost:", sum(distance_matrix[best_path[0][i]][best_path[0][i+1]] for i in range(len(best_path[0])-1)))
print("Robot 1 Tour:", best_path[1])
print("Robot 1 Total Travel Cost:", sum(distance_matrix[best_path[1][i]][best_path[1][i+1]] for i in range(len(best_path[1])-1)))
print("Overall Total Travel Cost:", best_path[3])