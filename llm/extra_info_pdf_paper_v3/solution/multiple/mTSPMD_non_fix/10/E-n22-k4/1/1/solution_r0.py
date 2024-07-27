import math
import random

cities = {0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
          6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
          12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
          18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_distance(tour):
    total = 0
    for i in range(len(tour) - 1):
        total += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total

def simulated_annealing(sol, T, cooling_rate, stopping_temp):
    current_sol = sol[:]
    current_cost = calculate_total_distance(current_sol)
    best_sol = sol[:]
    best_cost = current_cost
    
    while T > stopping_temp:
        next_sol = current_sol[:]
        # Generate two random indices and swap them to create a new tour
        i, j = random.sample(range(1, len(next_sol) - 1), 2)  # avoid swapping the depot
        next_sol[i], next_sol[j] = next_sol[j], next_sol[i]
        
        next_cost = calculate_pdf(next_sol)
        
        if next_cost < current_cost or random.random() < math.exp((current_cost - next_cost) / T):
            current_sol = next_sol[:]
            current_cost = next_confidence
            if current_cost < best_cost:
                best_sol = current_sol[:]
                best_cost = current_cost
                
        T *= cooling_rate
    
    return best_sol, best_cost

def partition_cities(num_robots, cities):
    # Partition cities into approximately equal segments, excluding depots which are starting points
    city_list = list(cities.keys())[4:]  # starts from city index 4
    random.shuffle(city_list)
    chunk_size = len(city_list) // num_robots
    return [city_list[i:i + chunk_size] for i in range(0, len(city_list), chunk_size)]

partitions = partition_cities(4, cities)
robot_tours = []
total_cost = 0

for idx, part in enumerate(partitions):
    tour = [0] + part + [0]  # starting and ending at the depot city index 0
    optimized_tour, tour_cost = simulated_annealing(tour, T=10000, cooling_rate=0.999, stopping_temp=1)
    robot_tours.append((idx, optimized_tour, tour_cost))
    total_cost += tour_cost

# Output results
for robot, tour, cost in robot_tours:
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")