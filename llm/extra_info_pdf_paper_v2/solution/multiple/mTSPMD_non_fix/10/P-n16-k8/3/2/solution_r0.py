import math
import random

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Depot indices
depots = [0, 1, 2, 3, 4, 5, 6, 7]

# Initial robotic assignments: all start at depot 0
robot_assignments = [0 for _ in range(8)]  # 8 robots all starting from depot 0

# Define number of robots
num_robots = 8

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_cost_of_tour(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

def simulated_annealing(depot_index, available_cities):
    current_temp = 100
    cooling_rate = 0.995
    min_temp = 1
    current_solution = [depot_index] + random.sample(available_cities, len(available_cities))
    current_cost = total_cost_of_tour(current_solution)
    
    while current_temp > min_temp:
        new_solution = current_solution.copy()
        i, j = random.sample(range(1, len(new_solution)), 2)  # Skip the depot for swapping
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        new_cost = total_cost_of_tour(new_solution)
        
        if new_cost < current_cost or random.uniform(0, 1) < math.exp((current_cost - new_cost) / current_temp):
            current_solution, current_cost = new_solution, new_cost
            
        current_temp *= cooling_rate
    
    return current_solution, current_cost

# Logic to balance the load among robots before SA optimization
visited = [False] * len(cities)
assignments = [[] for _ in range(num_robots)]

for i in range(num_robots):
    robot_city_count = len(cities) // num_robots + (1 if i < len(cities) % num_robots else 0)
    assignments[i].append(depots[i % len(depots)])  # Start from a depot
    count = 0
    while count < robot_city_count:
        city = random.choice([c for c in range(len(cities)) if not visited[c] and c not in depots])
        assignments[i].append(city)
        visited[city] = True
        count += 1

# Run SA for each robot
overall_cost = 0
result = []
for i in range(num_robots):
    if len(assignments[i]) <= 1: continue  # No tour if only one city in the assignment
    tour, cost = simulated_annealing(assignments[i][0], assignments[i][1:])
    result.append((i, tour, cost))
    overall_cost += cost

# Output results
for robot, tour, cost in result:
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_cost, 2)}")