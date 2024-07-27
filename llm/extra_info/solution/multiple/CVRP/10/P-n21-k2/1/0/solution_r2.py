import math

# Coordinate and demand data of the cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

num_robots = 2
capacity = 160
depot = 0

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Function to find the next city with the nearest heuristic
def find_next_city(tour_load, current_city, visited, demands):
    min_distance = float('inf')
    next_city = None
    for i in range(1, len(cities)):
        if not visited[i] and tour_load + demands[i] <= capacity:
            dist = distance_matrix[current_city][i]
            if dist < min_distance:
                min_distance = dist
                next_city = i
    return next_city

# Initialize robots with empty tours and tracking of loads
tours = [[depot] for _ in range(num_robots)]
current_loads = [0] * num_robots
visited_cities = [False] * len(cities)
visited_cities[depot] = True

# Assign cities to robots' routes
for _ in range(1, len(cities)):
    for robot_id in range(num_robots):
        current_city = tours[robot_id][-1]
        next_city = find_next_city(current_loads[robot_id], current_city, visited_cities, demands)
        if next_city is not None:
            tours[robot_id].append(next_city)
            visited_cities[next_city] = True
            current_loads[robot_id] += demands[next_city]
        else:
            break

# Close each robot's tour by returning to the depot
for robot_id in range(num_robots):
    tours[robot_id].append(depot)

# Function to calculate the travel cost of a tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Compute and display the results
total_cost = 0
for robot_id in range(num_robots):
    tour_cost = calculate_tour_cost(tours[robot_id], distance_matrix)
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")