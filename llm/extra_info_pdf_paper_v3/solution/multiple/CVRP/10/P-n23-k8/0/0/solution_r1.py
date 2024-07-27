import math

# City coordinates and demands
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot parameters
num_robots = 8
robot_capacity = 40

# Helper function to calculate the Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Determine each robot's tour and calculate distances
def make_tours(cities, demands, num_robots, robot_capacity):
    num_cities = len(cities)
    city_indices = list(range(1, num_cities))  # exclude depot city (index 0)
    tours = [[] for _ in range(num_robots)]
    tour_costs = [0] * num_robots
    capacities = [0] * num_robots
    current_locations = [0] * num_robots  # start all robots at depot

    # Assign cities to robots
    while city_indices:
        for i in range(num_robots):
            if not city_indices:
                break
            tour = [0]  # start from depot
            remaining_capacity = robot_capacity
            tour_cost = 0
            j = 0
            while j < len(city_indices):
                city_index = city_indices[j]
                if demands[city_index] <= remaining_capacity:
                    if len(tour) > 1:  # add distance from last city in tour
                        tour_cost += distance(cities[tour[-1]], cities[city_index])
                    else:  # first city from depot
                        tour_cost += distance(cities[0], cities[city_index])
                    tour.append(city_index)
                    remaining_capacity -= demands[city_index]
                    city_indices.pop(j)
                else:
                    j += 1
            tour.append(0)  # return to depot
            tour_cost += distance(cities[tour[-2]], cities[0])
            tours[i] = tour
            tour_costs[i] = tour_cost
            capacities[i] = robot_capacity - remaining_capacity

    return tours, tour_costs

tours, tour_costs = make_tours(cities, demands, num_robots, robot_capacity)
overall_total_cost = sum(tour_costs)

# Print the output
for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
    if tour and len(tour) > 2:  # Ensure the tour has intermediate cities
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")