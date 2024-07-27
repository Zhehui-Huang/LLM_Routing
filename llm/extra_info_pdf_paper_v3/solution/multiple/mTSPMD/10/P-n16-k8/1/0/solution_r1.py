import numpy as np
import random
from scipy.spatial.distance import euclidean

# City coordinates, where index corresponds to city number
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Robot start and end cities
robot_depot = {
    0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 
    5: 5, 6: 6, 7: 7
}

# Number of robots
num_robots = len(robot_depot)

def compute_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

def generate_tours():
    # Since every city must be visited once, create a simple initial tour list excluding depot cities
    all_cities = set(range(len(cities)))
    depot_cities = set(robot_depot.values())
    other_cities = list(all_cities - depot_cities)
    
    # Shuffle non-depot cities for initial random tours
    random.shuffle(other_cities)
    
    # Distribute cities round-robin to robots, starting after depot cities
    tours = {r: [robot_depot[r]] for r in range(num_robots)}
    robot_index = 0
    
    for city in other_cities:
        tours[robot_index].append(city)
        robot_index = (robot_index + 1) % num_robots
        
    # Ensuring each tour ends at its respective depot city
    for r in range(num_robots):
        tours[r].append(robot_depot[r])
    
    return tours

def calculate_total_cost(tours):
    total_cost = 0
    individual_costs = {}
    
    for r, tour in tours.items():
        tour_cost = sum(compute_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        individual_costs[r] = tour_cost
        total_cost += tour_cost
        
    return individual_costs, total_cost

# Generate the tours and calculate costs
tours = generate_tours()
individual_costs, total_cost = calculate_total_cost(tours)

# Output each robot's tour and costs
for robot_id in sorted(tours.keys()):
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {individual_costs[robot_id]:.2f}\n")

print(f"Overall Total Travel Cost: {total_cost:.2f}")