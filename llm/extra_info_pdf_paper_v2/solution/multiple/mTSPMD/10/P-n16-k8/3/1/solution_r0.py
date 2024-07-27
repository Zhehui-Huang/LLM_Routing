import math
import random

# City coordinates (total 16 cities)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots and their depots
num_robots = 8
depots = [i for i in range(num_robots)]  # robots start and end at depots 0 to 7

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initialize pheromones on paths and the desirability (heuristic) of each path
pheromones = [[1 for _ in range(len(coordinates))] for _ in range(len(coordinates))]
desirability = [[1 / distance(i, j) if i != j else 0 for j in range(len(coordinates))] for i in range(len(coordinates))]

# Ant Colony System parameters
alpha = 1.0  # Influence of pheromone
beta = 5.0   # Influence of heuristic
evaporation_rate = 0.5
pheromone_deposit = 1.0
num_iterations = 100
num_ants = 20

# Random seed for reproducibility
random.seed(42)

# ACS Algorithm for multi-depot mTSP
def ACS():
    best_tours = None
    best_cost = float('inf')
    
    # Iterate over the number of desired iterations
    for iteration in range(num_iterations):
        all_tours = []
        for _ in range(num_ants):
            # Each ant constructs a tour starting from each robot's depot
            tours = [[] for _ in range(num_robots)]
            unvisited_cities = set(range(len(coordinates)))
            
            # Initial setup of starting depots
            for i in range(num_robots):
                tours[i].append(depots[i])
                unvisited_cities.remove(depots[i])

            # Construction of the tours
            for i in range(num_robots):
                current_city = depots[i]
                while unvisited_cities:
                    probabilities = []
                    for city in unvisited_cities:
                        prob = (pheromones[current_city][city] ** alpha) * (desirability[current_city][city] ** beta)
                        probabilities.append(prob)
                    
                    if sum(probabilities):
                        chosen_city = random.choices(list(unvisited_cities), weights=probabilities)[0]
                    else:
                        chosen_city = random.choice(list(unvisited_cities))
                    
                    tours[i].append(chosen_city)
                    unvisited_cities.remove(chosen_city)
                    current_city = chosen_city
                
                # Return to depot
                tours[i].append(depots[i])

            all_tours.append(tours)
        
        # Evaluate and update pheromones
        for tours in all_tours:
            total_cost = sum(sum(distance(tours[i][k], tours[i][k + 1]) for k in range(len(tours[i]) - 1)) for i in range(num_robots))
            if total_cost < best_cost:
                best_cost = total_cost
                best_tours = tours
            
            # Pheromone update
            for i in range(num_robots):
                for j in range(len(tours[i]) - 1):
                    pheromones[tours[i][j]][tours[i][j + 1]] += pheromone_deposit / total_cost

        # Pheromone evaporation
        for i in range(len(coordinates)):
            for j in range(len(coordinates)):
                pheromones[i][j] *= (1 - evaporation_rate)
    
    return best_tours, best_cost

# Run the ACS algorithm
best_tours, best_cost = ACS()

# Print result
overall_total_cost = 0
for i, tour in enumerate(best_tours):
    tour_cost = sum(distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")