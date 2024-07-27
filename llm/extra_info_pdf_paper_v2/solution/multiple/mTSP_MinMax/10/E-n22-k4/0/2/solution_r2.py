import math
import random

# Coordinates of the cities including the depot (city 0)
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Function to calculate the Euclidean distance between two cities
def calc_distance(city1, index2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[index2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize the tours for each robot, starting from the depot
robots_tours = [[] for _ in range(num_robots)]
index = 0

# Distribute cities (starting from index 1, as index 0 is the depot) among robots
for city in range(1, len(city_coords)):
    robots_tours[index].append(city)
    index = (index + 1) % num_robots

# Add depot to the start and end of each robot's tour
for tour in robots_tours:
    tour.insert(0, 0)
    tour.append(0)

# Calculate the travel cost for a given tour
def tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Simple function to execute a rudimentary swap optimization for demonstration
def optimize_tours(tours):
    for _ in range(1000):  # Number of random optimization iterations
        for tour_index in range(len(tours)):
            tour = tours[tour_index]
            if len(tour) > 4:  # Need at least 4 to make a swap (including depots)
                for _ in range(10):  # Number of tries per tour
                    i, j = sorted(random.sample(range(1, len(tour)-2), 2))
                    new_tour = tour[:i] + [tour[j]] + tour[i+1:j] + [tour[i]] + tour[j+1:]
                    if tour_cost(new_tour) < tour_cost(tour):
                        tours[tour_index] = new_tour
    return tours

# Optimize tours using a simple optimization algorithm
optimized_tours = optimize_tours(robots_tours)

# Calculate and print the costs and details of each tour
maximum_cost = 0  # Keep track of the maximum travel cost
for i, tour in enumerate(optimized_tours):
    cost = tour_cost(tour)
    maximum_cost = max(maximum_cost, cost)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

# Output the maximum cost among all robots
print(f"Maximum Travel Cost: {maximum_cost}")