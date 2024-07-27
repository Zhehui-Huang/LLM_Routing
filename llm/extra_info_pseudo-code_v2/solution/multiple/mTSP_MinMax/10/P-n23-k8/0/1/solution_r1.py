import math
import random

# Define the cities coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Distance calculation using Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Initialization based on nearest city to depot heuristic
def initialization():
    num_robots = 8
    tours = {i: [0] for i in range(num_robots)}
    assigned_cities = set()
    
    # Sort cities by their distance to the depot (city 0)
    unvisited_cities = list(range(1,len(cities)))
    unvisited_cities.sort(key=lambda i: distance(cities[0], cities[i]))

    robot_index = 0
    for city in unvisited_cities:
        tours[robot_index].append(city)
        assigned_cities.add(city)
        robot_index = (robot_index + 1) % num_robots
    
    for r in tours:
        tours[r].append(0)  # Return to the depot
    
    return tours

# Calculate the tour cost for a single tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(1, len(tour)):
        cost += distance(cities[tour[i-1]], cities[tour[i]])
    return cost

# Initialize and calculate tours
tours = initialization()
tour_costs = {r: calculate_tour_cost(tours[r]) for r in tours}
max_tour_cost = max(tour_costs.values())

# Print result tours and costs
for r in tours:
    print(f"Robot {r} Tour: {tours[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_costs[r]}")

print(f"Maximum Travel Cost: {max_tour_cost}")