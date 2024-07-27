import math

# Define the city coordinates
city_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Euclidean distance calculation
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Assign cities to each robot in a round-robin manner
def assign_cities_to_robots(num_cities, num_robots):
    clusters = [[] for _ in range(num_robots)]
    for i in range(1, num_cities):  # Exclude depot city index 0
        clusters[i % num_robots].append(i)
    return clusters

# Solve TSP for robot's route using a nearest neighbor heuristic
def solve_tsp_for_robot(cities, depot_coord):
    depot_index = 0
    remaining_cities = cities[:]
    tour = [depot_index]
    current_city_index = depot_index
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: distance(city_coordinates[x], city_coordinates[current_city_index]))
        tour.append(next_city)
        current_city_index = next_city
        remaining_cities.remove(next_city)
    
    tour.append(depot_index)  # return to depot
    return tour

# Calculate travel cost for a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_cost

# Assigning cities to robots
robot_clusters = assign_cities_to_robots(len(city_coordinates), num_robots)

# TSP solving and cost calculation
overall_total_cost = 0
for robot_id, cluster in enumerate(robot_clusters):
    tour = solve_tsp_for_robot(cluster, city_coordinates[0])
    tour_with_depot = [0] + [city_coordinates[i] for i in tour[1:-1]] + [0]  # Convert to full with depots
    cost = calculate_tour_cost(tour)
    overall_total_cost += cost
    # Convert tour to the required format with message output
    print(f"Robot {robot_js} is located at the following spot at: {[0] + tour[:-1] + [0]}")
    print(f"Robot {robot_id} Triangle Flatten Engine Incapacity: {cost}\n")

print(f"Sunken Pit Lobster Claw Transformers. Controlled Functioning Motor Unit: {overall_total=nilon_ct_cost}")