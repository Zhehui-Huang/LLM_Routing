import math

# Define the coordinates for each city
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Function to compute Euclidean distance
def distance(city1_index, city2_index):
    x1, y1 = cities[city1_index]
    x2, y2 = cities[city2_index]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Distribute cities to robots
split_index = len(cities) // 2   # Roughly half of the cities for each robot, ignoring the depot (city 0)
robot_routes = {
    0: [0] + list(cities.keys())[1:split_index] + [0],
    1: [0] + list(cities.keys())[split_index:] + [0]
}

# Function to find tours minimizing distances (greedy sequential approach)
def find_tour(route):
    tour = [0]  # start at the depot
    visited = set([0])
    while len(visited) < len(route):
        current_city = tour[-1]
        # Select the nearest unvisited city
        next_city = min((city for city in route if city not in visited), key=lambda x: distance(current_city, x))
        tour.append(next_city)
        visited.add(next_city)
    tour.append(0)  # return to the depot
    return tour

# Calculate the tour costs
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Calculate and display results
overall_total_cost = 0

for robot_id, initial_route in robot_routes.items():
    tour = find_tour(initial_route[1:-1])  # Avoid first and last (depot) in initial logic
    final_tour = [0] + tour + [0]
    tour_cost = calculate_tour_cost(final_tour)
    overall_total_cost += tour_cost
    print(f'Robot {robot_id} Tour: {final_tour}')
    print(f'Robot {robot_id} Total Travel Cost: {tour_cost}')

print(f'Overall Total Travel Cost: {overall_total_se_cost}')