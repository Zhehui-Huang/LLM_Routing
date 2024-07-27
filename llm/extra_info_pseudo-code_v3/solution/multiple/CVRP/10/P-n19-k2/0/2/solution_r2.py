import math

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Define demands at each city (excluding city 0 as it's a depot with demand 0)
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14,
    10: 8, 11: 7, 12: 14, 13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15
}

# Robot parameters
number_of_robots = 2
capacity = 160
robots_tours = {i: [] for i in range(number_of_robots)}
remaining_capacity = {i: capacity for i in range(number_of_robots)}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(a, b):
    return math.hypot(cities[a][0] - cities[b][0], cities[a][1] - cities[b][1])

# Initialize robots at the depot
for i in range(number_of_robots):
    robots_tours[i].append(0)

# Assign cities to robots ensuring demand and capacity are not exceeded
unvisited = list(demands.keys())
while unvisited:
    for robot in robots_tours:
        if not unvisited:
            break
        path = robots_tours[robot]
        current_city = path[-1]
        # Find nearest unvisited city that fits the remaining capacity
        options = [(city, calculate_distance(current_city, city)) for city in unvisited if demands[city] <= remaining_capacity[robot]]
        if not options:
            continue
        next_city = min(options, key=lambda x: x[1])[0]
        path.append(next_city)
        remaining_capacity[robot] -= demands[next_city]
        unvisited.remove(next_city)

# Ensure all robots return to the depot
for robot in robots_tours:
    if robots_tours[robot][-1] != 0:
        robots_tours[robot].append(0)

# Calculate total travel cost
total_cost = 0
for robot, tour in robots_tours.items():
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i + 1])
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")