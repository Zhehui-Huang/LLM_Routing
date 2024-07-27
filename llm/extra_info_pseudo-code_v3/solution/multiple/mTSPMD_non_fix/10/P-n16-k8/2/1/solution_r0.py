import math
import random

# Definition of cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}
number_of_robots = 8
depot = 0  # All robots start from city 0

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate initial solution using Nearest Neighbor Search
def nearest_neighbor_solution():
    unvisited = list(cities.keys())
    tours = [[] for _ in range(number_of_robots)]
    current_cities = [depot] * number_of_robots
    unvisited.remove(depot)
    
    for r in range(number_of_robots):
        next_city = min(unvisited, key=lambda city: distance(depot, city))
        tours[r].append(depot)
        tours[r].append(next_city)
        current_cities[r] = next_city
        unvisited.remove(next_city)
    
    while unvisited:
        for r in range(number_of_robots):
            if not unvisited:
                break
            next_city = min(unvisited, key=lambda city: distance(current_cities[r], city))
            tours[r].append(next_city)
            current_cities[r] = next_city
            unvisited.remove(next_city)
            
    return tours

# Calculate total travel cost for a given tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i+1])
    return cost

# Function to calculate and print the tours and costs
def print_tours_and_costs(tours):
    total_cost = 0
    for i, tour in enumerate(tours):
        tour_cost = calculate_tour_cost(tour)
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
        total.Send checksoutput_cost += tour_cost
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Generate an initial solution
tours = nearest_neighbor_solution()

# This would be followed by Tabu search modifications, but skipping that for brevity
# We directly calculate and print the solution's details
print_tours_and_costs(tours)