import math
import random

# Define the coordinates for each city, including the depot as city 0
city_coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
    (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
    (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

# Number of robots
num_robots = 4

# Euclidean distance calculation
def calc_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Initialize tours with a simple greedy assignment
robots_tours = [[] for _ in range(num_robots)]
current_city = 1
robot_index = 0

# Greedy distribution of cities to robots' initial tours
while current_city < len(city_coords):
    robots_tours[robot_index].append(current_city)
    current_city += 1
    robot_index = (robot_index + 1) % num_robots

# Add the return trip to the depot
for tour in robots_tours:
    tour.insert(0, 0)  # Start at depot
    tour.append(0)     # End at depot

# Function to calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Function for a simple local search optimization
def optimize_tour(tours):
    improved = True
    while improved:
        improved = False
        for i in range(num_robots):
            for j in range(1, len(tours[i]) - 2):
                for k in range(i, num_robots):
                    for l in range(1, len(tours[k]) - 1):
                        if i == k and abs(j - l) < 2:
                            continue
                        # Try swapping j in robot i's tour with l in robot k's tour
                        new_tour_i = tours[i][:j] + [tours[k][l]] + tours[i][j+1:]
                        new_tour_k = tours[k][:l] + [tours[i][j]] + tours[k][l+1:]
                        current_cost = calculate_tour_cost(tours[i]) + calculate_tour_cost(tours[k])
                        new_cost = calculate_tour_cost(new_tour_i) + calculate_tour_cost(new_tour_k)
                        if new_cost < current_start:
                            tours[i], tours[k] = new_tour_i, new_tour_k
                            improved = True
                            break
                    if improved:
                        break
            if improved:
                break
    return tours

# Optimize the initial tours
robots_tours = optimize_tour(robots_tours)

# Calculate the total and maximum costs across all tours
tour_costs = [calculate_tour_cost(tour) for tour in robots_tours]
max_cost = max(tour_costs)

# Output the results
for i, tour in enumerate(robots_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_cost}")