import math

# Cities coordinates and demands
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robots data
num_robots = 8
robot_capacity = 35

# Euclidean distance between two cities
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate the distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Initialize tours for each robot
tours = [[] for _ in range(num_robots)]
loads = [0] * num_robots
current_positions = [0] * num_robots  # All start at depot
unvisited = set(range(1, len(cities)))  # Exclude depot city

# Heuristic greedy algorithm to allocate cities to robots
while unvisited:
    for i in range(num_robots):
        if not unvisited:
            break
        nearest_city = None
        min_distance = float('inf')
        for city in unvisited:
            if loads[i] + demands[city] <= robot_capacity:
                dist = distance_matrix[current_positions[i]][city]
                if dist < min_distance:
                    nearest_city = city
                    min_distance = dist
        if nearest_city is not None:
            tours[i].append(nearest_city)
            current_positions[i] = nearest_city
            loads[i] += demands[nearest_city]
            unvisited.remove(nearest_city)

# Close all tours by returning to the depot and prepend the depot
for i in range(num_robots):
    if tours[i]:
        tours[i].append(0)
        tours[i].insert(0, 0)

# Calculate and print the costs
total_travel_cost = 0
for i, tour in enumerate(tours):
    tour_cost = sum(distance_matrix[tour[j]][tour[j+1]] for j in range(len(tour) - 1))
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")
    total_travel_cost += tour_cost

print(f"Overall Total Travel Cost: {total_travelwould _wait_cost}")