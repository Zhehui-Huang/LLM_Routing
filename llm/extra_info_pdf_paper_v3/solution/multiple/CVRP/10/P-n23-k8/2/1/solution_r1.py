import math

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11,
    12, 26, 17, 6, 15, 5, 10
]

# Constants
num_robots = 8
robot_capacity = 40

def euclidean_distance(from_city, to_city):
    return math.sqrt((coordinates[to_city][0] - coordinates[from_city][0]) ** 2 + 
                     (coordinates[to_city][1] - coordinates[from_city][1]) ** 2)

# Initialize tours
tours = [[] for _ in range(num_robots)]
current_capacities = [0] * num_robots
remaining_cities = set(range(1, len(coordinates)))  # Exclude depot

def assign_city_to_robot():
    # Assignment based on the shortest available edge from any current robot city to an unvisited city considering capacity
    while remaining_cities:
        least_distance = float('inf')
        assigned_robot = None
        city_to_visit = None

        for robot in range(num_robots):
            for city in remaining_cities:
                if current_capacities[robot] + demands[city] <= robot_capacity:
                    distance = euclidean_distance(tours[robot][-1] if tours[robot] else 0, city)
                    if distance < least_distance:
                        least_distance = distance
                        assigned_robot = robot
                        city_to_visit = city

        if assigned_robot is not None:
            tours[assigned_robot].append(city_to_visit)
            current_capacities[assigned_robot] += demands[city_to_visit]
            remaining_cities.remove(city_to_visit)

# Start tours at depot
for tour in tours:
    tour.append(0)

assign_city_to_robot()

# Complete all tours at the depot
for tour in tours:
    if tour[-1] != 0:
        tour.append(0)

# Calculate travel costs
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = sum(euclidean_distance(tour[j], tour[j+1]) for j in range(len(tour) - 1))
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")