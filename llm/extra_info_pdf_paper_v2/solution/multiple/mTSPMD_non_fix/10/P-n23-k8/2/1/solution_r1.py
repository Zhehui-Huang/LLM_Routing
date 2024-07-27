import numpy as np
import math
import random

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46),
    17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def simulated_annealing(num_robots=8, starting_city=0):
    all_cities = list(cities.keys())
    all_cities.remove(starting_city)
    
    per_robot = len(all_cities) // num_robots
    tours = [all_cities[i * per_robot:(i + 1) * per_robot] for i in range(num_robots)]
    for i in range(len(all_cities) % num_robots):
        tours[i].append(all_cities[-i-1])
    
    for i in range(num_robots):
        random.shuffle(tours[i])
        tours[i].insert(0, starting_city)
        tours[i].append(starting_city)
    
    temp = 10000
    cooling_rate = 0.995
    min_temp = 1
    
    def total_distance(tours):
        return sum(sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1)) for tour in tours)
    
    current_cost = total_distance(tours)
    
    while temp > min_temp:
        robot_index = random.randrange(num_robots)
        if len(tours[robot_index]) > 3:
            i, j = sorted(random.sample(range(1, len(tours[robot_index]) - 1), 2))
            new_tours = [tour[:] for tour in tours]
            new_tours[robot_index][i:j] = reversed(new_tours[robot_index][i:j])
        
            new_cost = total_distance(new_tours)
        
            if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                tours = new_tours
                current_cost = new_cost
        
        temp *= cooling_rate
    
    return tours, current_cost

tours, overall_cost = simulated_annealing()

for robot_id, tour in enumerate(tours):
    tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")