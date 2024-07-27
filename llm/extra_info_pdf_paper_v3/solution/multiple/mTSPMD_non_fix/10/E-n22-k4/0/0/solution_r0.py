import numpy as np
import random
import math

# Cities' coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Depots are part of cities
depots = [0, 1, 2, 3]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_route_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += euclidean_distance(cities[route[i-1]], cities[route[i]])
    return cost

def simulated_annealing_solve(cities, depots, num_robots):
    # Distribute cities among robots
    assignments = [[] for _ in range(num_robots)]
    non_depot_cities = list(set(range(len(cities))) - set(depots))
    random.shuffle(non_depot_cities)

    k = 0
    for city in non_depot_cities:
        assignments[k % num_robots].append(city)
        k += 1
    
    for d in depots:
        assignments[d % num_robots].insert(0, d)  # Start each with its depot

    # Perform simulated annealing for each robot's tour
    temp = 10000
    cooling_rate = 0.995
    min_temp = 1
    tours = [a[:] for a in assignments]

    while temp > min_temp:
        for i in range(num_robots):
            # Try swapping two cities in the tour
            if len(tours[i]) > 2:
                new_tour = tours[i][:]
                pos1, pos2 = random.sample(range(1, len(new_tour)), 2)
                new_tour[pos1], new_tour[pos2] = new_tour[pos2], new_tour[pos1]
                current_cost = total_route_cost(tours[i])
                new_cost = total_route_cost(new_tour)
                if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temp):
                    tours[i] = new_tour[:]
        temp *= cooling_rate
    
    # Calculate each robot's tour cost
    total_travel_costs = [total_route_cost(tour) for tour in tours]
    overall_total_travel_cost = sum(total_travel_costs)
    
    # Output the tours and costs
    result_str = ""
    for i in range(num_robots):
        result_str += f"Robot {i} Tour: {tours[i]}\n"
        result_str += f"Robot {i} Total Travel Cost: {total_travel_costs[i]}\n"
    result_str += f"Overall Total Travel Cost: {overall_total_travel_cost}\n"
    
    return result_str

# Apply the SA-based solution
result_output = simulated_annealing_solve(cities, depots, len(depots))
print(result_output)