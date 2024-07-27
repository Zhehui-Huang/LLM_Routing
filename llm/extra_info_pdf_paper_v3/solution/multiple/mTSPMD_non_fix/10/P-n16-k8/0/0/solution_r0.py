import numpy as np
import math
import matplotlib.pyplot as plt

# City Coordinates
cities_coordinates = {
    0: (30, 40),  1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),  5: (52, 33),
    6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),  10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Distance Function (using Euclidean distance)
def distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initial Tour Generation (Round-Robin Assignment)
def initial_tours(num_robots, num_cities):
    tours = [[] for _ in range(num_robots)]
    for i in range(num_cities):
        tours[i % num_robots].append(i)
    return tours

def simulated_annealing(tour, temp_decay=0.99, initial_temp=1000, min_temp=1):
    current_temp = initial_temp
    current_tour = tour[:]
    current_cost = tour_cost(current_tour)
    
    while current_temp > min_temp:
        new_tour = current_tour[:]
        # Swap two cities
        i, j = np.random.randint(0, len(tour), size=2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        
        new_cost = tour_cost(new_tour)
        cost_difference = new_cost - current_cost
        
        if cost_difference < 0 or np.random.random() < math.exp(-cost_difference / current_temp):
            current_tour = new_tour
            current_cost = new_cost
        
        current_temp *= temp_decay
    
    return current_tour, current_cost

# Calculate the cost of a tour
def tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance(tour[i-1], tour[i])
    return cost

# Number of Robots and Cities
num_robots = 8
num_cities = 16
initial_city_per_robot = 2  # Equal distribution of initial cities to robots

all_tours = initial_tours(num_robots, num_cities)
final_tours = []
total_cost = 0

for i, tour in enumerate(all_tours):
    tour.append(0)  # Make sure the tour starts are 0 and ends at 0 for simplicity
    improved_tour, cost = simulated_annealing(tour)
    final_tours.append(improved_tour)
    total_cost += cost
    print(f"Robot {i} Tour: {improved_tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")