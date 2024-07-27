import math
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Define cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242), 
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208), 
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 
    20: (155, 185), 21: (139, 182)
}

# Define demand of each city
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 
    100, 500, 600, 1200, 1300, 1300, 300, 900, 
    2100, 1000, 900, 2500, 1800, 700
]

# Robot information
num_robots = 4
robot_capacity = 6000

# Function to calculate the total cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Greedy heuristic to assign initial tours for robots
def initial_solution(cities, demands, num_robots, robot_capacity):
    tours = [[] for _ in range(num_robots)]
    demands_left = demands[:]
    remaining_capacity = [robot_capacity] * num_robots

    for city, demand in sorted(enumerate(demands), key=lambda x: -x[1]):
        if city == 0:
            continue
        assigned = False
        for i in range(num_robots):
            if remaining_capacity[i] >= demand:
                if len(tours[i]) == 0:
                    tours[i].extend([0, city, 0])
                else:
                    tours[i].insert(-1, city)
                remaining_capacity[i] -= demand
                assigned = True
                break
        if not assigned:
            # Infeasible initial solution, try different touring or increase number of robots/capacity
            raise RuntimeError("Initial solution not feasible, increase number of robots or their capacity.")
    return tours

# Generate initial tours
tours = initial_solution(cities, demands, num_robots, robot_capacity)

# Calculate costs
total_costs = [calculate_tour_cost(tour) for tour in tours]
overall_total_cost = sum(total_costs)

# Output the results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")