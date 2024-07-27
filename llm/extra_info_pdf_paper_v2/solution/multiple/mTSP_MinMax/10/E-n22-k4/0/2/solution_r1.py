import math
import random

# Define the coordinates for each city, including the depot as city 0
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 244), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

num_robots = 4

# Function to calculate Euclidean distance between cities
def calc_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Initialize tours: each robot starts at the depot
robots_tours = [[] for _ in range(num_robots)]
current_city = 1
robot_index = 0

# Greedily distribute cities to robots' tours
while current_city < len(city_coords):
    robots_tours[robot_index].append(current_city)
    current_city += 1
    robot_index = (robot_index + 1) % num_robots

# Insert the depot as the starting and concluding location of each tour
for tour in robots_tours:
    tour.insert(0, 0)  # Start at depot
    tour.append(0)     # Return to depot

# Calculate cost for a given tour
def calculate_tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Display initial tours before optimization
print("Initial tours:")
for idx, tour in enumerate(robots_tours):
    cost = calculate_tour_cost(tour)
    print(f"Robot {idx} Tour: {tour}, Cost: {cost}")

# Simple local search swap for enhancing the solution
def optimize_tour(tours):
    changed = True
    while changed:
        changed = False
        for i in range(num_robots):
            for j in range(1, len(tours[i]) - 2):
                for k in range(i, num_robots):
                    for l in range(1, len(tours[k]) - 1):
                        if i == k and abs(j - l) < 2:
                            continue
                        # Try swapping
                        new_tours = [tour[:] for tour in tours]
                        new_tours[i][j], new_tours[k][l] = new_tours[k][l], new_tours[i][j]
                        # Calculate new and old costs
                        old_cost = calculate_tour_cost(tours[i]) + calculate_tour_cost(tours[k])
                        new_cost = calculate_tour_cost(new_tours[i]) + calculate_tour_cost(new_tours[k])
                        if new_cost < old_cost:
                            tours[i][j], tours[k][l] = tours[k][l], tours[i][j]
                            changed = True
    return tours

# Optimize the robots' tours
optimized_tours = optimize_tour(robots_tours)

# Calculate and display optimized tours and costs
tour_costs = [calculate_tour_cost(tour) for tour in optimized_tours]
max_cost = max(tour_costs)

print("\nOptimized Tours:")
for i, tour in enumerate(optimized_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_code}")