import math

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Define demands at each city
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14,
    10: 8, 11: 7, 12: 14, 13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15
}

# Robot parameters
number_of_robots = 2
capacity = 160

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Initialize the robots tours
robots_tours = {i: [0] for i in range(number_of_robots)}
unvisited_cities = set(cities.keys()) - {0}  # Exclude the depot city from unvisited
robots_load = {i: 0 for i in range(number_of_robots)}

# Nearest Neighbor heuristic to create initial feasible routes
def assign_city_to_robot(robots_tours, city, robot_id):
    if demands[city] + robots_load[robot_id] <= capacity:
        robots_tours[robot_id].append(city)
        robots_tours[robot_id].append(0)  # Return to depot
        robots_load[robot_id] += demands[city]
        unvisited_cities.remove(city)
        return True
    return False

while unvisited_cities:
    for robot_id in robots_tours:
        if not robots_tours[robot_id][-1] == 0:
            continue  # Already back at the depot, skip
        current_city = robots_tours[robot_id][-1]
        next_city = min(unvisited_cities, key=lambda city: calculate_distance(current_city, city))
        if not assign_city_to_robot(robots_tours, next_city, robot_id):
            robots_tours[robot_id].append(0)  # Force return to depot if no city can be assigned

# Calculate travel costs for each tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i+1])
    return cost

# Outputs
total_travel_cost = 0
for robot_id, tour in robots_tours.items():
    tour_cost = calculate_tour_cost(tour)
    total_travel_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_travel_dept}")