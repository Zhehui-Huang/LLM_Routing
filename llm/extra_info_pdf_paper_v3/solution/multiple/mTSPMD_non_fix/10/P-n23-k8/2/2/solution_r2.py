import math
import random
from itertools import permutations
from copy import deepcopy

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to calculate the total distance of the tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance(tour[i-1], tour[i])
    return cost

# Number of robots
num_robots = 8

# Initial distribution of cities among robots (naive distribution)
cities_per_robot = len(cities) // num_robots
remaining_cities = list(cities.keys())[1:]  # Exclude the depot city 0
random.shuffle(remaining_cities)

# Assign cities to robots
robots_tours = {i: [0] for i in range(num_robots)}

for idx, city in enumerate(remaining_cities):
    robots_tours[idx % num_robots].append(city)

# Improve tour by Tabu Search
def tabu_search(tour, iterations=1000, tabu_size=10):
    best_cost = calculate_tour_cost(tour)
    best_tour = tour[:]
    tabu_list = []
    
    for _ in range(iterations):
        city1, city2 = random.sample(tour[1:], 2)  # Random cities excluding depot
        idx1, idx2 = tour.index(city1), tour.index(city2)
        new_tour = tour[:]
        new_tour[idx1], new_tour[idx2] = new_tour[idx2], new_tour[idx1]  # Swap cities
        
        new_cost = calculate_tour_cost(new_tour)
        if new_cost < best_cost and new_tour not in tabu_list:
            best_tour = new_tour[:]
            best_cost = new_cost
            if len(tabu_list) >= tabu_size:
                tabu_list.pop(0)
            tabu_list.append(new_tour)
    
    return best_tour, best_cost

# Apply Tabu Search to each robot's tour
overall_cost = 0
for robot_id in robots_tours:
    tour, cost = tabu_search(robots_tours[robot_id])
    robots_tours[robot_id] = tour
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
    overall_cost += cost

print(f"Overall Total Travel Cost: {overall_cost}")