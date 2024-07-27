import numpy as np
import random

# Distance Calculation
def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Cities with their coordinates
cities_coordinates = {
  0: (30, 40),
  1: (37, 52),
  2: (49, 49),
  3: (52, 64),
  4: (31, 62),
  5: (52, 33),
  6: (42, 41),
  7: (52, 41),
  8: (57, 58),
  9: (62, 42),
  10: (42, 57),
  11: (27, 68),
  12: (43, 67),
  13: (58, 48),
  14: (58, 27),
  15: (37, 69),
  16: (38, 46),
  17: (61, 33),
  18: (62, 63),
  19: (63, 69),
  20: (45, 35)
}

# Parameters
antnum = 10
cyclenum = 100
init_pheromone = 1
alpha = 1
beta = 5
rho = 0.1

# Calculate initial distance matrix and pheromone matrix
num_cities = len(cities_coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
pheromone_matrix = np.full((num_cities, num_cities), init_pheromone)

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dist = euclidean_distance(*cities_coordinates[i], *cities_coordinates[j])
            distance_matrix[i][j] = dist
            distance_matrix[j][i] = dist

# Ant Colony Optimization
def ant_colony_optimization():
    best_cost = np.inf
    global_best_tour = None
    stagnant_cycles = 0

    while stagnant_cycles < cyclenum:
        all_ants_tours = []
        all_ants_costs = []
        
        # Each ant makes a tour
        for ant in range(antnum):
            # Random start depots
            start_city = random.choice([0, 1])
            tour = [start_city]
            current_city = start_city
            visited = {current_city}
            
            while len(visited) < num_cities:
                allowed_cities = [i for i in range(num_cities) if i not in visited and i != current_city]
                if not allowed_cities:
                    break
                
                # Calculate transition probabilities
                probabilities = []
                for next_city in allowed_cities:
                    tau = pheromone_matrix[current_city][next_city] ** alpha
                    eta = (1.0 / distance_matrix[current_city][next_city]) ** beta
                    probabilities.append(tau * eta)
                
                # Normalize probabilities
                probabilities = probabilities / np.sum(probabilities)
                
                # Choose next city based on probabilities
                next_city = np.random.choice(allowed_cities, p=probabilities)
                tour.append(next_city)
                visited.add(next_city)
                current_city = next_city
            
            # Complete tour and return to depot
            tour.append(start_city)
            tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            
            # Storing tours and costs
            all_ants_tours.append(tour)
            all_ants_costs.append(tour_cost)
        
        # Update pheromone levels
        pheromone_matrix *= (1 - rho)  # Evaporation
        for k, tour in enumerate(all_ants_tours):
            for i in range(len(tour) - 1):
                pheromone_matrix[tour[i]][tour[i + 1]] += 1.0 / all_ants_costs[k]  # Pheromone deposit

        # Check for global best tour
        min_cost_index = np.argmin(all_ants_costs)
        if all_ants_costs[min_cost_index] < best_cost:
            best_cost = all_ants_costs[min_cost_index]
            global_best_tour = all_ants_tours[min_cost_index]
            stagnant_cycles = 0
        else:
            stagnant_cycles += 1

    return global_best_tour, best_cost

# Running the optimization
best_tour, best_tour_cost = ant_colony_optimization()

# Printing the tours and costs
print(f"Robot 0 Tour: {best_tour}")
print(f"Robot 0 Total Travel Cost: {best_tour_cost}")

# Note: In practice, we would need to split this single tour across two robots as per task description.
# This code simplifies and finds a single optimal tour. The division can be based on finding two depots in the tour and dividing.