import math
from random import shuffle, randint, choice

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += euclidean_distance(coordinates[route[i]], coordinates[route[i+1]])
    return total_cost

def initialize_solution(num_robots, coordinates):
    cities = list(range(1, len(coordinates)))  # Exclude depot city 0
    shuffle(cities)
    tours = [[] for _ in range(num_robots)]
    for index, city in enumerate(cities):
        tours[index % num_robots].append(city)
    for tour in tours:
        tour.insert(0, 0)  # Starting at depot
        tour.append(0)     # Returning to depot
    return tours

# Generate initial solution
num_robots = 2
tours = initialize_solution(num_robots, coordinates)

# Calculate costs
tour_costs = [calculate_route_cost(tour) for tour in tours]
max_cost = max(tour_costs)

# Output
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")