import numpy as np
import math

# Coordinates of cities including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

num_cities = len(coordinates)
num_robots = 4
starting_depot = 0  # All robots start from depot city 0

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Initial solution based on Nearest Neighbour Search (NNS)
def nearest_neighbour_solution():
    unvisited_cities = set(range(1, num_cities))  # Exclude the starting depot
    tours = [[starting_depot] for _ in range(num_robots)]  # Start each tour at the depot
    
    # Distributing cities to initial depots
    for tour in tours:
        if not unvisited_cities:
            break
        nearest_city = min(unvisited_cities, key=lambda x: distance(tour[-1], x))
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
    
    # Completing the tours with remaining cities
    while unvisited_cities:
        for tour in tours:
            if not unvisited_cities:
                break
            nearest_city = min(unvisited_cities, key=lambda x: distance(tour[-1], x))
            tour.append(nearest_city)
            unvisited_cities.remove(nearest_city)
    
    return tours

# Calculate total travel cost of the tours
def calculate_total_cost(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        tour_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        individual_costs.append(tour_cost)
        total_cost += tour_cost
    return individual_costs, total_cost

# Initialization and simulation of the Tabu Search
def simulate_tabu_search():
    # Generate initial solution
    initial_tours = nearest_neighbour_solution()
    best_tours = initial_tours
    individual_costs, best_cost = calculate_total_cost(best_tours)
    
    print("Initial solution:")
    for i, tour in enumerate(initial_tours):
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {individual_costs[i]}")
    
    print(f"Overall Total Travel Cost: {best_cost}")

simulate_tabu_search()