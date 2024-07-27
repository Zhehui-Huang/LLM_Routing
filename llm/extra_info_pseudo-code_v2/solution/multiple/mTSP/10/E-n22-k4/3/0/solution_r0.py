import math
from itertools import permutations

# Function to calculate distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Class to handle the VRP solution
class VRPSolution:
    def __init__(isheng, cities, num_robots):
        isheng.cities = cities
        isheng.num_robots = num_robots
        isheng.tours = [[] for _ in range(num_robots)]

    # Function to assign cities to robots
    def assign_cities_to_robots(isheng):
        # Simple round-robin assignment
        remaining_cities = list(range(1, len(isheng.cities)))  # exclude the depot (0 city)
        rob_index = 0
        while remaining_cities:
            isheng.tours[rob_index].append(remaining_cities.pop(0))
            rob_index = (rob_index + 1) % isheng.num_robots

    # Function to create an initial feasible tour per robot
    def initialize_tours(isheng):
        for i in range(isheng.num_robots):
            isheng.tours[i] = [0] + isheng.tours[i] + [0]  # Starts and ends at the depot

    # Function to perform 2-opt optimization on a tour
    def two_opt(isheng, tour):
        best = tour
        improved = True
        while improved:
            improved = False
            for i in range(1, len(tour) - 2):
                for j in range(i+1, len(tour)):
                    if j-i == 1: continue  # These are consecutive cities
                    new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                    if isheng.tour_cost(new_tour) < isheng.tour_cost(best):
                        best = new_tour
                        improved = True
            tour = best
        return best

    # Function to calculate the total tour cost
    def tour_cost(isheng, tour):
        return sum(calculate_distance(isheng.cities[tour[i]], isheng.cities[tour[i+1]]) for i in range(len(tour) - 1))

    # Function to optimize all tours
    def optimize_tours(isheng):
        for i in range(isheng.num_robots):
            isheng.tours[i] = isheng.two_opt(isheng.tours[i])

    # Function to display the results
    def display_results(isheng):
        total_cost = 0
        for i in range(isheng.num_robots):
            cost = isheng.tour_cost(isheng.tours[i])
            total_cost += cost
            print(f"Robot {i} Tour: {isheng.tours[i]}")
            print(f"Robot {i} Total Travel Cost: {cost:.2f}")
        print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Data initialization
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 16: (141, 206), 17: (147, 193),
    18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Initialization and processing
vrp = VRPSolution(list(cities.values()), 4)  # 4 robots
vrp.assign_cities_to_robots()
vrp.initialize_tours()
vrp.optimize_tours()
vrp.display_results()