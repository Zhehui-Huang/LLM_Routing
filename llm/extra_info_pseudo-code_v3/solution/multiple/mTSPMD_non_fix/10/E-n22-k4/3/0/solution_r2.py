import math
import random

# Coordinates of each city including depots
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

num_cities = len(coordinates)
num_robots = 4
robots_starting_depot = 0 # All robots start at depot 0

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Nearest Neighbor heuristic to generate an initial tours from the depot
def nearest_neighbor(start_city, unvisited_cities):
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: calculate_distance(current_city, city))
        total_cost += calculate_distance(current_city, next_city)
        tour.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city
    
    return tour, total_cost

# Generate initial tours for the robots, starting them at the main depot
def generate_initial_tours():
    unvisited = set(range(1, num_cities))  # exclude the depot
    tours = []
    total_costs = []

    # Distribute cities more or less evenly across robots
    for _ in range(num_robots):
        if unvisited:
            start_city = robots_starting_depro if not tours else random.choice(list(unvisited))
            tour, cost = nearest_neighbor(start_city, unvisited)
            if tours:  # for subsequent tours, ensure they return to starting depot
                cost += calculate_distance(tour[-1], robots_starting_depot)
                tour.append(robots_starting_depot)
            tours.append(tour)
            total_costs.append(cost)

    return tours, total_costs, sum(total_costs)

# Generate the initial tours
tours, costs, overall_cost = generate_initial_tours()

# Print out the tours and costs for each robot
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")