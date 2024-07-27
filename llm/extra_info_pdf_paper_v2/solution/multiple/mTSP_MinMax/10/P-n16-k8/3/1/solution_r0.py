import math
import random

# Definition of cities and their coordinates
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of cities and robots
num_cities = len(cities_coordinates)
num_robots = 8

# Calculate Euclidean distance between two cities
def distance(city1, city0):
    x1, y1 = cities_coordinates[city1]
    x0, y0 = cities_coordinates[city0]
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

# Initialize tours for robots
tours = [[] for _ in range(num_robots)]

# Distribute cities evenly among the robots, excluding the depot city (at index 0)
cities_to_visit = list(range(1, num_cities))
random.shuffle(cities_to_visit)

for index, city in enumerate(cities_to_visit):
    robot_index = index % num_robots
    tours[robot_index].append(city)

# Function to calculate total tour distance
def calculate_tour_cost(tour):
    total_cost = 0
    if tour:
        total_cost += distance(0, tour[0])  # Depot to first city
        for i in range(len(tour) - 1):
            total_cost += distance(tour[i], tour[i + 1])
        total_cost += distance(tour[-1], 0)  # last city back to depot
    return total_cost

# Fine-tune the tours using a simple local search
def local_search(tours):
    improved = True
    while improved:
        improved = False
        for i in range(num_robots):
            for j in range(i + 1, num_robots):
                for city_i in range(len(tours[i])):
                    for city_j in range(len(tours[j])):
                        # Swap cities and check new costs
                        new_tours = [list(tour) for tour in tours]
                        new_tours[i][city_i], new_tours[j][city_j] = new_tours[j][city_j], new_tours[i][city_i]
                        old_cost_max = max(calculate_tour_cost(tours[k]) for k in range(num_robots))
                        new_cost_max = max(calculate_tour_cost(new_tours[k]) for k in range(num_robots))
                        if new_cost * 0.99 < old_cost_max:  # Allow a small deterioration
                            tours = new_tours
                            improved = True
                            break
                    if improved:
                        break
                if improved:
                    break
            if improved:
                break
    return tours

# Improve the tours
tours = local_search(tours)

# Output and evaluate results
tour_costs = [calculate_tour_cost(tour) for tour in tours]
max_cost = max(tour_costs)

for i in range(num_robots):
    print(f"Robot {i} Tour: {[0] + tours[i] + [0]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")