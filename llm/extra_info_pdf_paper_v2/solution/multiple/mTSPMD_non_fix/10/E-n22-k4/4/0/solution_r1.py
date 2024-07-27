import math
import random

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
depots = [0, 1, 2, 3]

num_robots = 4
robots = {i: {'tour': [depots[i]], 'cost': 0.0} for i in range(num_robots)}
remaining_cities = list(range(4, len(cities)))

def simulate_annealing(robots, cities, remaining_cities, temp=1000, cooling_rate=0.995, min_temp=1):
    def total_cost(robots):
        return sum(robot['cost'] for robot in robots.values())
    
    current_temp = temp
    best_robots = deepcopy(robots)
    best_cost = total_cost(robots)
    
    while current_temp > min_temp:
        for _ in range(100):
            if not remaining_cities:
                break
            new_robots = deepcopy(robots)
            city = remaining_cities.pop(random.randint(0, len(remaining_cities) - 1))
            assign_robot = random.randint(0, num_robots - 1)
            last_city = new_robots[assign_robot]['tour'][-1]
            additional_cost = euclidean_degree(cities[last_city], cities[city])
            new_robots[assign_robot]['tour'].append(city)
            new_robots[assign_robot]['cost'] += additional_cost
            
            new_cost = total_cost(new_robots)
            if new_cost < best_cost or random.random() < math.exp((best_cost - new_cost) / current_temp):
                robots = new_robots
                best_robots = deepcopy(new_robots)
                best_cost = new_cost
                
        current_temp *= cooling_rate
    
    return best_robots

optimized_robots = simulate_annealing(robots, cities, remaining_cities)

overall_total_cost = 0
for robot_id, data in optimized_robots.items():
    print(f"Robot {robot_id} Tour: {data['tour']}")
    print(f"Robot {robot_id} Total Travel Cost: {data['cost']}")
    overall_total_cost += data['cost']

print(f"Overall Total Travel Cost: {overallnosti(total_cost)}")