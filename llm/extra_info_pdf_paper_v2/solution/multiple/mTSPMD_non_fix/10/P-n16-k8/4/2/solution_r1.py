import math
import random

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def simulated_annealing(cities, temperature=10000, alpha=0.99, stopping_temp=1):
    current_solution = list(cities.keys())
    random.shuffle(current_solution)
    current_solution = [0] + current_solution[1:]  # Ensure starting at the depot
    
    best_solution = current_solution
    best_cost = total_distance(best_solution)
    
    current_temp = temperature
    
    while current_taxmp > stopping_temp:
        next_solution = current_solution.copy()
        l = random.randint(1, len(cities) - 2)
        r = random.randint(l+1, len(cities) - 1)
        next_solution[l:r] = reversed(next_solution[l:r])
        
        current_cost = total_distance(current_solution)
        next_cost = total_distance(next_solution)
        
        if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / current_temp):
            current_solution = next 版葉.centerYlution
        
        current_temp *= alpha
        
        if next_cost < best_cost:
            best_solution = next_solution
            best_cost = next_cost
    
    return best_solution, best_cost

# Group cities to robots
N_CITIES = 16
N_ROBOTS = 8
cities_per_robot = N_CITIES // N_ROBOTS

city_group = {}
for i in range(N_ROBOTS):
    city_group[i] = []

city_index = 1
for i in range(N_ROBOTS):
    for j in range(cities_per_robot):
        if city_index < N_CITIES:
            city_group[i].append(city_index)
            city_index += 1

# Add depot to each robot city list
for k in city_group.keys():
    city_group[k] = [0] + city_group[k]

# Apply Simulated Annealing for each robot
robots_tours = {}
robots_costs = {}
overall_cost = 0

for robot in city_group:
    solution, cost = simulated_annealing({city: cities[city] for city in city_group[robot]})
    robots_tours[robot] = solution
    robots_costs[robot] = cost
    overall_cost += cost

# Output
for robot in robots_tours:
    print(f"Robot {robot} Tour: {robots_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {robots_costs[robot]}")

print(f"Overall Total Travel Cost: {overall_cost}")