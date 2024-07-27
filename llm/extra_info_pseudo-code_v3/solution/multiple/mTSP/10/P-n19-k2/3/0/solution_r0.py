import math
import random

# Define the coordinates of each city including the depot
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
          (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Euclidean distance function
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate an initial solution where each robot gets different sequences
def generate_initial_solution(cities, num_robots):
    non_depot_cities = list(range(1, len(cities)))
    random.shuffle(non_depot_cities)
    chunks = [non_depot_cities[i::num_robots] for i in range(num_robots)]
    tours = [[0] + chunk + [0] for chunk in chunks]
    return tours

# Calculate the total travel cost of one tour
def calculate_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Printing functions
def print_results(tours):
    total_cost = 0
    for i, tour in enumerate(tours):
        cost = calculate_cost(tour)
        total_cost += cost
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost:.2f}")
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Main function to solve the MTSP
def solve_mtsp(cities, num_robots):
    tours = generate_initial_solution(cities, num_robots)
    print_results(tours)

# Call the main function
solve_mtsp(cities, 2)