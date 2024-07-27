import math
import random

# Defined cities with their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Number of robots and their start depots
depots = {0: 0, 1: 1}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def simulated_annealing(cities, start_depot):
    current_solution = cities[:]
    random.shuffle(current_solution)
    current_cost = sum(euclidean_distance(current_solution[i], current_solution[i+1]) for i in range(len(current_solution)-1))
    
    # Initial temperature and cooling rate
    T = 10000
    cooling_rate = 0.995
    minimal_temperature = 1
    
    while T > minimal_temperature:
        i, j = random.randrange(0, len(cities)), random.randrange(0, len(cities))
        new_solution = current_solution[:]
        new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
        new_cost = sum(euclidean_distance(new_solution[i], new_solution[i+1]) for i in range(len(new_solution)-1))
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / T):
            current_solution = new_solution
            current_cost = new_cost
        
        T *= cooling_rate
    
    return [start_depot] + current_solution, current_cost

# Distribute cities among robots
all_cities = list(cities.keys())
robot_cities = {0: [], 1: []}
for city in all_cities:
    if city not in depots.values():
        robot_cities[city%2].append(city)

# Run optimization for each robot
robot_tours = {}
total_overall_cost = 0
for robot_id, start_depot in depots.items():
    tour, cost = simulated_annealing(robot_cities[robot_id], start_depot)
    robot_tours[robot_id] = tour
    total_overall_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_overall_cost}")