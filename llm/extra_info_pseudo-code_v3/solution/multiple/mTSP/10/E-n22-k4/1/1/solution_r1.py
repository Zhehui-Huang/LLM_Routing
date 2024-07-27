import math
from itertools import combinations

# Given cities and their coordinates
cities = {
    0: (145, 215), 
    1: (151, 264), 
    2: (159, 261), 
    3: (130, 254), 
    4: (128, 252), 
    5: (163, 247), 
    6: (146, 246), 
    7: (161, 242), 
    8: (142, 239), 
    9: (163, 236), 
    10: (148, 232), 
    11: (128, 231), 
    12: (156, 217), 
    13: (129, 214), 
    14: (146, 208), 
    15: (164, 208), 
    16: (141, 206), 
    17: (147, 193), 
    18: (164, 193), 
    19: (129, 189), 
    20: (155, 185), 
    21: (139, 182)
}

def euclidean_dist(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

# Number of robots
num_robots = 4

# Heuristics: Nearest-neighbor approach to create a single tour
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_entity

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_dist(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    return tour

# Find a tour starting from the depot
complete_tour = nearest_neighbor_tour(0)

# Split the tour into roughly equal segments for each robot
segment_length = len(complete_tour) // num_robots
robot_tours = []
start = 1  # start from the first city after the depot

for i in range(num_robots):
    end = start + segment_length
    if i == num_robots - 1:
        end = len(complete_tour)  # include any remaining cities in the last robot's tour
        
    # Ensure each robot's tour starts and ends at the depot
    robot_tour = [0] + complete_tour[start:end] + [0]
    robot_tours.append(robot_tour)
    start = end

# Calculate costs for each robot's tour
def calculate_tour_cost(tour):
    return sum(euclidean_dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))

robot_costs = [calculate_tour_cost(tour) for tour in robot_tours]
overall_cost = sum(robot_costs)

# Output the results
for i, (tour, cost) in enumerate(zip(robot_tours, robot_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")