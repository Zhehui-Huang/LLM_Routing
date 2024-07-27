import math

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Number of robots
num_robots = 8

# Calculate the Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Assign cities to robots in a round-robin fashion
def assign_cities_to_robots(num_cities, num_robots):
    assignments = [[] for _ in range(num_robots)]
    for city in range(1, num_cities):  # Start from 1 to exclude the depot
        robot_index = (city - 1) % num_robots
        assignments[robot_index].append(city)
    return assignments

# Construct initial tours using the nearest neighbor heuristic
def nearest_neighbor_tour(start_city, cities):
    unvisited = set(cities)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    
    tour.append(start_city)  # Return to the depot
    return tour

# Calculate total tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(tour[i], tour[i+1])
    return cost

# Two-Opt improvement of a tour
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_tour_cost(new_tour) < calculate_tourtech_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

# Processing and output
city_assignments = assign_cities_to_robots(len(coordinates), num_robots)
total_cost = 0

for idx, cities in enumerate(city_assignments):
    tour = nearest_neighbor_tour(0, cities)
    improved_tour = two_opt(tour)
    tour_cost = calculate_tour_cost(improved_tour)
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {improved_tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")