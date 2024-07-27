import numpy as np
import random

# Coordinates of cities including depots
coordinates = [
    (30, 40), (37, 52),
    (49, 43), (52, 64),
    (31, 62), (52, 33),
    (42, 41), (52, 41),
    (57, 58), (62, 42),
    (42, 57), (27, 68),
    (43, 67), (58, 27),
    (37, 69), (61, 33),
    (62, 63), (63, 69),
    (45, 35)
]

# Parameters for the algorithm
antnum = 20
cyclenum = 100
inittrail = 0.1
alpha = 1.0
beta = 5.0
rho = 0.5

# Number of cities and depots
num_cities = len(coordinates)
depots = [0, 1]

# Initialize distance matrix
distance_matrix = np.zeros((num_cities, num_cities))

# Calculate Euclidean Distance between each pair of cities
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = np.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)
        else:
            # No travel cost to travel to the same city
            distance_matrix[i][j] = float('inf')

# Helper function to calculate the travel cost of a tour
def calculate_travel_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance_matrix[tour[i-1]][tour[i]]
    return cost

# Initialization of pheromone levels
pheromone_levels = np.full((num_cities, num_cities), inittrail)

def main_aco_algorithm():
    best_solution = None
    best_cost = float('inf')
    num_no_improve = 0
    
    for cycle in range(cyclenum):
        solutions = []
        costs = []
        
        for ant in range(antnum):
            # Randomly decide the starting depot for each ant
            start_depot = random.choice(depots)
            tour = [start_depot]
            allowed = set(range(num_cities)) - set(tour) - set(depots)

            current = start_depot
            while allowed:
                probabilities = []
                for j in allowed:
                    tau_ij = pheromone_levels[current][j]
                    eta_ij = 1 / distance_matrix[current][j] if distance_matrix[current][j] > 0 else 0
                    probabilities.append((tau_ij ** alpha) * (eta_ij ** beta))
                
                if sum(probabilities) == 0:
                    probabilities = [1] * len(probabilities)
                
                probabilities = np.array(probabilities) / sum(probabilities)
                next_city = np.random.choice(list(allowed), p=probabilities)
                tour.append(next_city)
                current = next_city
                allowed.remove(next_city)
            
            tour.append(start_depot)  # Complete the tour by returning to depot
            solutions.append(tour)
            cost = calculate_travel_cost(tour)
            costs.append(cost)
        
        # Find the best solution in the current iteration
        current_best = min(costs)
        current_solution = solutions[costs.index(current_best)]
        if current_best < best_cost:
            best_cost = current_best
            best_solution = current_solution
            num_no_improve = 0
        else:
            num_no_improve += 1
        
        # Update pheromone trails
        pheromone_levels *= (1 - rho)  # Evaporation
        # Adding new pheromone
        for i, solution in enumerate(solutions):
            for j in range(1, len(solution)):
                pheromone_levels[solution[j - 1]][solution[j]] += 1 / costs[i]

        # Termination condition check
        if num_no_improve > cyclenum:
            break

    return best_solution, calculate_travel_cost(best_solution)

tour, cost = main_aco_algorithm()

print(f"Best Tour: {tour}")
print(f"Total Travel Cost: {cost}")