import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates for each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Calculate Euclidean distance
def calculate_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        cost += euclidean(coordinates[path[i]], coordinates[path[i+1]])
    return cost

# Greedy approach to generate an approximate initial solution
def greedy_solution(num_robots, depot, cities):
    tours = [[] for _ in range(num_robots)]
    remaining_cities = set(cities)
    current_locations = [depot] * num_robots

    while remaining_cities:
        for robot in range(num_robots):
            if not remaining_cities:
                break
            next_city = min(remaining_cities, key=lambda x: euclidean(coordinates[current_locations[robot]], coordinates[x]))
            tours[robot].append(next_city)
            current_locations[robot] = next_city
            remaining_cities.remove(next_city)

    # Closing the loop back to the depot
    for tour in tours:
        tour.insert(0, depot)  # Start at the depot
        tour.append(depot)     # Return to the depot

    return tours

# Function to solve the Multi-Vehicle TSP
def solve_multiple_tsp(num_robots, depot, cities):
    # Generate a greedy initial solution
    tours = greedy_solution(num_robots, depot, cities)
    
    # Calculate costs for each tour
    costs = [calculate_cost(tour) for tour in tours]
    overall_cost = sum(costs)

    # Print each robot's tour and costs
    for idx, tour in enumerate(tours):
        print(f"Robot {idx} Tour: {tour}")
        print(f"Robot {idx} Total Travel Cost: {costs[idx]:.2f}")

    print(f"Overall Total Travel Cost: {overall_cost:.2f}")

# Solve the TSP for 2 robots starting from depot city 0
solve_multiple_tsp(2, 0, list(range(1, 21)))