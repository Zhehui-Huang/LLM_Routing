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

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Pheromone matrix and distance matrix initialization
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i, j] = distance(i, j)

# Ant Colony Optimization parameters
num_ants = 20
num_iterations = 50
decay = 0.1
alpha = 1
beta = 2
initial_pheromone = 1 / (n_cities * 100)

pheromones = np.ones((n_cities, n_cities)) * initial_pheromone

def aco_solve():
    best_cost = float('inf')
    best_tours = None

    for iteration in range(num_iterations):
        for ant in range(num_ants):
            tours = [[0], [1]]
            remaining_cities = set(range(2, n_cities))
            
            for tour in tours:
                while remaining_cities:
                    current_city = tour[-1]
                    
                    transition_probs = []
                    total_prob = 0
                    for next_city in remaining_cities:
                        prob = (pheromones[current_city][next_city] ** alpha) * ((1.0 / distance_matrix[current_city][next_city]) ** beta)
                        transition_probs.append(prob)
                        total_prob += prob
                    
                    if total_prob == 0:  # Avoid division by zero
                        break
                    
                    # Select next city based on probabilities
                    probs = [prob / total_prob for prob in transition_probs]
                    next_city = np.random.choice(list(remaining_cities), p=probs)
                    tour.append(next_city)
                    remaining_cities.remove(next_city)
                
                tour.append(tour[0])  # Return to depot
                
            # Calculate tours cost
            tour_costs = [sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) for tour in tours]
            total_cost = sum(tour_costs)

            if total_cost < best_cost:
                best_cost = total_cost
                best_tours = tours

            # Pheromone update
            for tour in tours:
                for i in range(len(tour) - 1):
                    pheromones[tour[i]][tour[i + 1]] += 1.0 / total_cost
                    
        # Pheromone evaporation
        pheromones *= (1 - decay)
            
    return best_tours, best_cost

# Perform ACO
best_tours, best_cost = aco_solve()

# Output results
tour_costs = [sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)) for tour in best_tours]
overall_cost = sum(tour_costs)

for idx, tour in enumerate(best_tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")
print(f"Overall Total Travel Cost: {overall_cost}")