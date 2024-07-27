import math
import random

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of 16 cities including depots
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]

# Define parameters
num_robots = 8
start_depot = 0  # All robots start from depot city 0

# Calculate distances between all city pairs
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def simulated_annealing(tour, initial_temp, cooling_rate, stopping_temp):
    current_temp = initial_temp
    current_tour = tour
    current_cost = tour_cost(current_tour)
    
    while current_temp > stopping_temp:
        next_tour = neighbor_tour(current_tour)
        next_cost = tour_cost(next_tour)
        
        if next_cost < current_cost or math.exp((current_cost - next_cost) / current_temp) > random.random():
            current_tour = next_tour
            current_cost = next_cost
        
        current_temp *= (1 - cooling_rate)
    
    return current_tour, current_cost

def neighbor_tour(tour):
    i, j = sorted(random.sample(range(1, len(tour)), 2))
    new_tour = tour[:]
    new_tour[i:j] = reversed(tour[i:j])
    return new_tour

def tour_cost(tour):
    return sum(distances[tour[i]][tour[i - 1]] for i in range(1, len(tour)))

# Create initial tours (simple round-robin distribution of cities to robots)
robot_tours = {i: [start_depot] for i in range(num_robots)}
for i, city in enumerate(cities[start_depot+1:], start=start_depot+1):
    robot_tours[i % num_robots].append(city)

# Ensure all tours are valid and append the start_depot to the end
for i in range(num_robots):
    robot_tours[i].append(start_depot)

# Optimize each robot's tour using Simulated Annealing
overall_total_cost = 0
for i in range(num_robots):
    final_tour, tour_cost = simulated_annealing(robot_tours[i], 10000, 0.003, 1)
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {final_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")