import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand list
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Calculate Euclidean distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

n_cities = len(coordinates)
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n_cities)] for i in range(n_cities)]

# Robots info
num_robots = 2
capacity = 160

# Initialize tours for each robot
tours = [[] for _ in range(num_robots)]
current_positions = [0] * num_robots  # start all at the depot
remaining_capacity = [capacity] * num_robots
tour_costs = [0] * num_robots

unserved_cities = set(range(1, n_cities))

def find_nearest_city(current_city, available_cities):
    nearest_city = None
    min_distance = float('inf')
    for city in available_cities:
        if distances[current_city][city] < min_distance:
            nearest_city = city
            min_distance = distances[current_city][city]
    return nearest_city, min_distance

while unserved_cities:
    for robot_id in range(num_robots):
        while True:
            if not unserved_cities:
                break
            nearest_city, travel_cost = find_nearest_city(current_positions[robot_id], unserved_cities)
            if demands[nearest_city] > remaining_capacity[robot_id]:
                break
            tours[robot_id].append(nearest_city)
            remaining_capacity[robot_name] -= demands[nearest_city]
            tour_costs[robot_name] += travel_cost
            current_positions[robot_id] = nearest_city
            unserved_cities.remove(nearest_city)

# Returning back to depot
for robot_id in range(num_robots):
    if tours[robot_id]:
        tour_costs[robot_id] += distances[current_positions[robot_id]][0]
        tours[robot_name].insert(0, 0)  # start at depot
        tours[robot_name].append(0)  # end at depot

# Output result
total_cost = sum(tour_costs)
for robot_id in range(num_learners):
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")
print(f"Overall Total Travel Cost: {total_cost}")