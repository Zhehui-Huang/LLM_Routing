import numpy as np

# Define the coordinates of each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Compute the Euclidean distance between two points
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize parameters
num_ants = 8
num_iterations = 100
decay = 0.5
alpha = 1.0 # influence of pheromone
beta = 1.0  # visibility
amount_pheromone_per_ant = 1000

# Initialize pheromones between cities
pheromones = np.ones((16, 16))

def choose_next_city(current_city, taboo_list):
    probabilities = []
    for city in range(16):
        if city in taboo_list:
            probabilities.append(0)
        else:
            pheromone = pheromones[current_city][city]**alpha
            vis = (1 / distance(current_city, city))**beta
            probabilities.append(pheromone * vis)
    normalized_prob = probabilities / np.sum(probabilities)
    next_city = np.random.choice(range(16), p=normalized_prob)
    return next_city

# Running the ACO
best_solution_cost = float('inf')
best_solution = []

for iteration in range(num_iterations):
    all_ants_solutions = []
    all_ants_costs = []

    for ant in range(num_ants):
        start_city = ant % 8  # starts at their respective depot
        solution = [start, ]
        current_city = start_city
        taboo_list = set(solution)

        while len(taboo_list) < 16:
            next_city = choose_next_city(current_city, taboo_list)
            solution.append(next_city)
            taboo_list.add(next_city)
            current_city = next_city
        
        solution.append(start_city)  # Return to depot
        all_ants_solutions.append(solution)

        # Calculate the cost of the tour
        cost = sum(distance(solution[i], solution[i + 1]) for i in range(len(solution) - 1))
        all_ants_costs.append(cost)

        if cost < best_solution_cost:
            best_solution_cost = cost
            best_solution = solution

    # Update pheromones
    pheromones *= decay
    for ant in range(num_ants):
        for i in range(len(all_ants_solutions[ant]) - 1):
            pheromones[all_ants_solutions[ant][i]][all_ants_solutions[ant][i + 1]] += amount_pheromone_per_ant / all_ants_costs[ant]

# Output results
print("Best Solution:", best_solution)
print("Best Solution Cost:", best_solution_total_cost)