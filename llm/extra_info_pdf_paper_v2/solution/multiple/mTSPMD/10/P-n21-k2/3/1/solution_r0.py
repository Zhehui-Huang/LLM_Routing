import numpy as np

# City coordinates (index corresponds to city number)
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
])

# Function to calculate Euclidean distance between two cities
def calculate_distance(coords1, coords2):
    return np.sqrt(np.sum((coords1 - coords2)**2))

# Initialize pheromone levels on the paths and distance matrix
num_cities = coordinates.shape[0]
pheromone_levels = np.ones((num_cities, num_cities))
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance = calculate_distance(coordinates[i], coordinates[j])
            distance_matrix[i, j] = distance

# ACO parameters
num_ants = 25
evaporation_rate = 0.5
alpha = 1.0  # Pheromone importance
beta = 2.0   # Distance importance
iterations = 100

# Robots info
depots = [0, 1]
num_robots = 2

# ACO implementation
def ant_colony_optimization():
    best_tours = None
    best_cost = np.inf
    
    for _ in range(iterations):
        all_tours = []
        tour_costs = []
        
        for i in range(num_ants):
            tours = []
            remaining_cities = set(range(num_cities)) - set(depots)
            costs = []
            
            # Each robot constructs a tour starting from its depot
            for depot in depots:
                tour = [depot]  # Start at the depot
                current_city = depot
                
                while remaining_cities:
                    probabilities = []
                    for city in remaining_cities:
                        tau = pheromone_levels[current_city, city] ** alpha
                        eta = (1.0 / distance_matrix[current_city, city]) ** beta
                        probabilities.append(tau * eta)
                    
                    probabilities = np.array(probabilities) / sum(probabilities)
                    next_city = np.random.choice(list(remaining_cities), p=probabilities)
                    tour.append(next_city)
                    current_city = next_city
                    remaining_cities.remove(next_city)
                
                tour.append(depot)  # Return to depot
                tours.append(tour)
                costs.append(sum(distance_matrix[tour[j], tour[j+1]] for j in range(len(tour) - 1)))
            
            all_tours.append(tours)
            tour_costs.append(sum(costs))
        
        # Update best tours
        iteration_best_cost = min(tour_costs)
        if iteration_best_cost < best_cost:
            best_cost = iteration_best_cost
            best_tours = all_tours[np.argmin(tour_costs)]
        
        # Update pheromones
        pheromone_levels *= evaporation_rate
        for tours, cost in zip(all_tours, tour_costs):
            for tour in tours:
                for j in range(len(tour) - 1):
                    pheromone_levels[tour[j], tour[j+1]] += 1.0 / cost
    
    return best_tours, best_cost

best_tours, best_cost = ant_colony_optimization()

for i, tour in enumerate(best_tours):
    print(f"Robot {i} Tour: {tour}")
    tour_cost = sum(distance_matrix[tour[j], tour[j + 1]] for j in range(len(tour) - 1))
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {best_cost:.2f}")