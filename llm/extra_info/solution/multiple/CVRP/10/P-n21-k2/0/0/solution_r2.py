import math

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# City coordinates and demands (index starts at 0 for the depot)
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), 
          (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot specifications
robot_capacity = 160
num_robots = 2

# Initialize tours for each robot
tours = [[] for _ in range(num_robots)]
loads = [0] * num_robots
positions = [0] * num_robots  # All robots start at the depot

# Algorithm to Assign Cities to Robots
unassigned_cities = set(range(1, len(cities)))  # Exclude the depot

while unassigned_cities:
    for robot_index in range(num_robots):
        min_dist = float('inf')
        next_city = None
        for city in unassigned_cities:
            if demands[city] + loads[robot_index] <= robot_capacity:
                dist = distance(cities[positions[robot_arr]], cities[city])
                if dist < min_dist:
                    min_dist = dist
                    next_city = city
        if next_city is not None:
            tours[robot_index].append(next_city)
            loads[robot_index] += demands[next_city]
            positions[robot_index] = next_city
            unassigned_cities.remove(next_city)

# Ensure all robots return to the depot
for tour in tours:
    tour.append(0)

# Calculate travel costs
def calculate_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(cities[tour[i]], cities[tour[i + 1]])
    return cost

# Display results
total_travel_cost = 0
for idx, tour in enumerate(tours):
    robot_tour = [0] + tour
    cost = calculate_tour_cost(robot_tour, cities)
    total_travel_cost += cost
    print(f"Robot {idx} Tour: {robot_tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_cost:.2f}")