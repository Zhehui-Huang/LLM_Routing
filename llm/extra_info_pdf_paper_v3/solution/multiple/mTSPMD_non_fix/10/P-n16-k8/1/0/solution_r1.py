import math
import random

# Define cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Simulated Annealing implementation for TSP
def simulated_annealing(initial_tour, start_temp, rate_of_cooling, end_temp):
    current_temp = start_temp
    current_route = initial_tour[:]
    current_cost = calculate_total_distance(current_route)
    
    while current_temp > end_temp:
        new_route = current_route[:]
        # Swap two cities to generate a neighbor tour
        city1, city2 = random.sample(range(1, len(new_route)-1), 2)
        new_route[city1], new_route[city2] = new_route[city2], new_route[city1]
        new_cost = calculate_total_distance(new_route)
        
        # Acceptance probability
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / current_temp):
            current_route = new_path
            current_cost = new_cost
        
        # Cooling step
        current_temp *= rate_of_cooling

    return current_route, current_cost

# Function to compute the total distance of the tour
def calculate_total_distance(tour):
    total_dist = 0
    for i in range(len(tour) - 1):
        total_dist += distance(cities[tour[i]], cities[tour[i+1]])
    return total_dist

# Divide cities into tours, one per robot
def assign_cities_to_robots(num_robots):
    perm = random.sample(range(1, len(cities)), len(cities)-1)  # Exclude depot
    step = len(perm) // num_robots

    tours = [[0] + perm[i:i + step] for i in range(0, len(perm), step)]
    if len(tours) > num_robots:
        tours[-2].extend(tours[-1])
        tours.pop()
    for tour in tours:
        tour.append(0)  # Adding depot to end of tour for each robot
    return tours

def find_optimal_tours():
    tours = assign_cities_to_robots(num_robots)
    total_travel_cost = 0

    for index, tour in enumerate(tours):
        optimized_tour, tour_cost = simulated_annealing(tour, 10000, 0.995, 1)
        print(f"Robot {index} Tour: {optimized_tour}")
        print(f"Robot {index} Total Travel Cost: {tour_cost}\n")
        total_travel_cost += tour_cost
    
    print(f"Overall Total Travel Cost: {total_travel siempre}")

# Execute
find_optimal_tours()