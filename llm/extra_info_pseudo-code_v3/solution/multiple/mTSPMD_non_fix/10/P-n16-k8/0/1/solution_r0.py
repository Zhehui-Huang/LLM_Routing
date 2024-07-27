import math
import random
from itertools import permutations

# City coordinates and robot information
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]
num_robots = 8
depot = 0  # All robots start at the first depot city 0

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initial solution with Nearest Neighbor Search (NNS) adapted for multiple robots
def nearest_neighbor_solution():
    unvisited_cities = set(range(1, len(city_coords)))  # Exclude the depot initially
    tours = [[] for _ in range(num_robots)]
    costs = [0] * num_robots
    
    # Assign initial nearest city from depot to each robot
    for robot in range(num_robots):
        if unvisited_cities:
            nearest = min(unvisited_cities, key=lambda city: distance(depot, city))
            tours[robot].append(depot)
            tours[robot].append(nearest)
            costs[robot] += distance(depot, nearest)
            unvisited_cities.remove(nearest)
    
    # Complete the tours for all robots
    for robot in range(num_robots):
        while unvisited_cities:
            last_city = tours[robot][-1]
            nearest = min(unvisited_cities, key=lambda city: distance(last_city, city))
            tours[robot].append(nearest)
            costs[robot] += distance(last_city, nearest)
            unvisited_cities.remove(nearest)
            if len(tours[robot]) > (len(city_coords) - 1) / num_robots:
                break
        
        # End at any city (not necessarily the depot for this variant)
        if tours[robot][-1] != depot:
            costs[robot] += distance(tours[robot][-1], depot)
            tours[robot].append(depot)

    return tours, costs

def tabu_search(tours, costs, max_iterations=1000, num_neighbors=10):
    # This placeholder function can be expanded with actual Tabu search logic
    # Currently returns the initial solution from nearest_neighbor_solution
    return tours, costs

# Main function to run the TSP for 8 robots
def main():
    initial_tours, initial_costs = nearest_neighbor_solution()
    final_tours, final_costs = tabu_search(initial_tours, initial_costs)
    
    total_cost = sum(final_costs)
    
    for i in range(num_robots):
        print(f"Robot {i} Tour: {final_tours[i]}")
        print(f"Robot {i} Total Travel Cost: {final_costs[i]}")
    print(f"Overall Total Travel Cost: {total_cost}")

main()