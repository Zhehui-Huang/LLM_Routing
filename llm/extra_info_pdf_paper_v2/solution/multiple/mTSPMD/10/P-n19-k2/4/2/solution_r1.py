import numpy as np

# Euclidean distance helper
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Initialize cities and coordinates
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate distances matrix
num_cities = len(city_coordinates)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = euclidean_distance(city_coordinates[i], city_coordinates[j])

# Parameters for ACO
num_robots = 2
ants_per_robot = 20
iterations = 100
alpha = 1   # Pheromone importance
beta = 2    # Distance priority
evaporation_rate = 0.5
pheromone_deposit = 1
pheromone = np.ones((num_cities, num_cities))  # Initial pheromone levels

best_tours = None
best_cost = np.inf

# ACO Algorithm execution
for iteration in range(iterations):
    for ant in range(ants_per_robot):
        tours = [[0], [1]]  # Starting points for each robot
        remaining_cities = set(range(2, num_cities))
        
        # Generate tours for each ant for each robot
        for robot in range(num_robots):
            while remaining_cities:
                current_city = tours[robot][-1]
                transition_probabilities = []
                for next_city in remaining_cities:
                    probability = (pheromone[current_city][next_city] ** alpha) * \
                                  ((1 / distances[current_city][next_city]) ** beta)
                    transition_probabilities.append(probability)
                
                total_probability = sum(transition_probabilities)
                transition_probabilities = [prob / total_probability for prob in transition_probabilities]
                
                next_city = np.random.choice(list(remaining_cities), p=transition_probabilities)
                tours[robot].append(next_city)
                remaining_cities.remove(next_city)

        # Close the tours for each robot
        for robot in range(num_robots):
            tours[robot].append(tours[robot][0])
            
        # Calculate the cost of the tours
        cost = 0
        for robot in range(num_robots):
            tour_cost = sum(distances[tours[robot][i]][tours[robot][i+1]] for i in range(len(tours[robot])-1))
            cost += tour_cost
            
        # Update best tours if current is better
        if cost < best_cost:
            best_cost = cost
            best_tours = tours
            
        # Update pheromone trails
        for robot in range(num_robots):
            for i in range(len(tours[robot])-1):
                pheromone[tours[robot][i]][tours[robot][i+1]] += pheromone_deposit / cost
        
    # Evaporate pheromone
    pheromone *= (1 - evaporation_rate)

# Print each robot's tour and costs
overall_cost = 0
for robot in range(num_robots):
    tour = best_tours[robot]
    cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")