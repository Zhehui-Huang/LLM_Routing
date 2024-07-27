import math
from itertools import permutations

# Define cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Total number of robots
num_robots = 2

# Greedy initial solution splitting the cities (except the depot) between two robots
def initial_solution():
    city_ids = list(cities.keys())[1:]  # Exclude the depot in initial list
    tours = [[0] for _ in range(num_robots)]
    total_distances = [0] * num_robots
    
    # Sort cities based on the heuristic of closest next city
    remaining_cities = city_ids.copy()
    for i in range(len(city_ids)):
        robot_ind = i % num_robots
        if tours[robot_ind][-1] == 0 and remaining_cities:
            # Start from the depot, find the nearest city
            nearest_city = min(remaining_cities, key=lambda x: calculate_distance(0, x))
        else:
            # Find the nearest city from the last added city
            last_city = tours[robot_ind][-1]
            nearest_city = min(remaining_cities, key=lambda x: calculate_distance(last_city, x))
        
        tours[robot_ind].append(nearest_greedy_city)
        remaining_cities.remove(nearest_greedy_city)

    # Complete each tour by returning to the depot
    for robot in range(num_robots):
        tours[robot].append(0)
        for j in range(len(tours[robot]) - 1):
            total_distances[robot] += calculate_distance(tours[robot][j], tours[robot][j+1])
    
    return tours, total_distances

tours, total_distances = initial_solution()
overall_total_cost = sum(total_distances)

# Print the results
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {total_distances[robot]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")