import numpy as np
from itertools import permutations

# Define the cities' coordinates and corresponding demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8,
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6,
    15, 5, 10
]
num_robots = 8
robot_capacity = 40

# Define a function to compute Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Initial solution generator using a simple heuristic (Nearest Neighbour)
def generate_initial_solution():
    robots_tours = [[] for _ in range(num_robots)]
    demands_met = [False] * len(demands)
    demands_met[0] = True  # Depot demand is always met (no demand)
    
    for robot in range(num_robots):
        current_city = 0
        current_load = 0
        tour = [0]  # Start at the depot

        while True:
            # Find nearest unvisited city that we can fulfill its demand
            closest_city = None
            min_dist = float('inf')
            
            for i in range(1, len(coordinates)):
                if not demands_met[i] and current_load + demands[i] <= robot_capacity:
                    dist = distance(current_city, i)
                    if dist < min_dist:
                        min_dist = dist
                        closest_city = i
            
            if closest_city is None:
                break  # No more cities can be added to this tour

            tour.append(closest_city)
            current_load += demands[closest_city]
            demands_met[closest_city] = True
            current_city = closest_city

        tour.append(0)  # Return to depot
        robots_tours[robot] = tour
        
        if all(demands_met):
            break  # All cities have been visited

    return robots_tours

# Calculate total cost for given tours
def calculate_cost(tours):
    total_cost = 0
    costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance(tour[i], tour[i+1])
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

# Generate an initial solution
tours = generate_initial_solution()
costs, total_cost = calculate_cost(tours)

# Outputting results
print("Results:")
for idx, tour in enumerate(tours):
    if tour and len(tour) > 2:  # at least one city is visited
        tour_cost = costs[idx]
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")