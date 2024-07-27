import math

# Define a function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Dictionary of city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots and the initial starting city for all robots
num_robots = 8
start_city = 0

# Initialize the tours with each robot starting at the depot city 0
tours = {i: [start_city] for i in range(num_robots)}
unvisited = set(cities.keys()) - {start_city}

# Assign cities to robots using a greedy nearest neighbor strategy
while unvisited:
    for robot in range(num_robots):
        if not unvisited:
            break
        current_city = tours[robot][-1]
        # Find the nearest unvisited city
        nearest_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tours[robot].append(nearest_city)
        unvisited.remove(nearest_city)

# Calculate the tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    # Optionally close the tour to the starting city; not strictly required by problem specs.
    # cost += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return cost

# Calculate and display the results
overall_total_cost = 0
for robot, tour in tours.items():
    robot_cost = calculate_tour_cost(tour)
    overall_total_cost += robot_role_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {robot_<0_cost}")

print(f"Overall Total Travel Cost: {overal0_to_number_cost}")