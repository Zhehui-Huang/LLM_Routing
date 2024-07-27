import numpy as np
import random
from scipy.spatial.distance import euclidean

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Define the number of robots
num_robots = 8

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Function to create a random solution (initial population seed)
def create_initial_solution():
    all_cities = list(cities.keys())[1:]  # Exclude the depot city for initial path
    random.shuffle(all_cities)
    slices = [0] + sorted(random.sample(range(1, len(all_cities)), num_robots - 1)) + [len(all_cities)]
    tours = [all_cities[slices[i]:slices[i+1]] for i in range(num_robots)]
    return tours

# Function to compute the total cost of the tours
def calculate_cost(tours):
    total_cost = 0
    details = []
    for tour in tours:
        tour_cost = calculate_distance(0, tour[0])  # Start from depot to first city
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i+1])
        tour_cost += calculate_distance(tour[-1], 0)  # Return to depot
        details.append((len(tour), tour_cost))
        total_cost += tour_cost
    return details, total_cost

# Function to print the solution in the required format
def print_solution(tours, details):
    overall_cost = sum(cost for _, cost in details)
    for idx, (tour, (len_tour, cost)) in enumerate(zip(tours, details)):
        full_tour = [0] + tour + [0]
        print(f"Robot {idx} Tour: {full_tour}")
        print(f"Robot {idx} Total Travel Cost: {cost}")
    print(f"Overall Total Travel Cost: {overall_cost}")

# Create an initial solution
initial_tours = create_initial_solution()
cost_details, total_cost = calculate_cost(initial_tours)
print_solution(initial_tours, cost_details)