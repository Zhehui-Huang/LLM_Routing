import math
import random

# Coordinates of the cities
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Number of cities and robots
num_cities = len(coordinates)
num_robots = 2
depots = [0, 1]

# Simulated Annealing Parameters
initial_temp = 100.0
final_temp = 1.0
alpha = 0.995
num_steps = 5000

def simulated_annealing():
    # Random initial solution (split the cities between two robots)
    cities = list(range(2, num_cities))  # exclude depots (0 and 1)
    random.shuffle(cities)
    split_point = len(cities) // 2
    tours = [cities[:split_point], cities[split_point:]]
    tours[0] = [0] + tours[0] + [0]  # tour for robot 0
    tours[1] = [1] + tours[1] + [1]  # tour for robot 1
    
    def total_cost(tours):
        # Calculate the total cost of the given set of tours
        cost = 0
        for tour in tours:
            for i in range(1, len(tour)):
                cost += euclidean_distance(tour[i-1], tour[i])
        return cost
    
    def random_swap(tours):
        # Randomly selects a city from each tour (excluding depots), and swaps them
        for _ in range(100):
            i, j = random.randint(1, len(tours[0])-2), random.randint(1, len(tours[1])-2)
            tours[0][i], tours[1][j] = tours[1][j], tours[0][i]
    
    current_temp = initial_temp
    while current_temp > final_temp:
        new_tours = [list(tour) for tour in tours]
        random_swap(new_tours)
        new_cost = total_cost(new_tours)
        old_cost = total_cost(tours)
        if new_cost < old_cost or math.exp((old_cost - new_cost) / current_temp) > random.random():
            tours = new_tours
        current_temp *= alpha
    
    return tours, total_cost(tours)

# Solve the problem
tours, total_cost = simulated_annealing()

# Output the results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    tour_cost = sum(euclidean_distance(tours[i][j], tours[i][j+1]) for j in range(len(tours[i])-1))
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")