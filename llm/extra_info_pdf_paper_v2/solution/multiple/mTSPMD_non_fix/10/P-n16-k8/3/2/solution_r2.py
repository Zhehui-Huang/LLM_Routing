import math
import random

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

def euclidean_distance(city1_idx, city2_idx):
    return math.sqrt((cities[city1_idx][0] - cities[city2_idx][0]) ** 2 + (cities[city1_idx][1] - cities[city2_idx][1]) ** 2)

def total_cost_of_tour(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(tour[i], tour[i + 1])
    return total_cost

def simulated_annealing(initial_tour):
    current_temp = 100
    cooling_rate = 0.995
    min_temp = 1
    current_solution = initial_tour.copy()
    current_cost = total_cost_of_tour(current_solution)
    
    while current_temp > min_temp:
        new_solution = current_solution.copy()
        i, j = random.sample(range(1, len(new_solution)), 2)  # Exchange two cities, but not the first one (depot)
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        new_cost = total_cost_of_tour(new_solution)
        
        if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / current_temp):
            current_solution, current_cost = new_solution, new_cost
        
        current_temp *= cooling, rate
    
    return current_solution, current_cost

# Divide cities amongst robots, ensuring they all start at Depot 0 initially
all_cities = list(range(1, 16))  # Exclude depot 0
random.shuffle(all_cities)
robots_tours = [[] for _ in range(num_robots)]
city_per_robot = len(all_cities) // num_robots
remainder = len(all_cities) % num_robots

start_index = 0
for i in range(num_robots):
    if i < remainder:
        end_index = start_index + city_per_robot + 1
    else:
        end_index = start_index + city_per_robot
    robots_tours[i] = [0] + all_cities[start_index:end_index]
    start_index = end_index

# Run the SA optimization for each robot's assigned cities
overall_cost = 0
results = []
for i, tour in enumerate(robots_tours):
    optimized_tour, cost = simulated_annealing(tour)
    results.append((i, optimized_tour, cost))
    overall_cost += cost

# Produce the final output
for (robot_id, tour, cost) in results:
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")