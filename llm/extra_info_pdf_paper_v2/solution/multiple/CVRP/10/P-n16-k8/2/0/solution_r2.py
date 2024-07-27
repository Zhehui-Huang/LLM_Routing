import math

# Data: Cities, Coordinates, and Demands
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

demands = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15,
    8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

# Robot information
num_robots = 8
capacity = 35
depot = 0

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize robots with start and end at the depot
tours = {i: [depot] for i in range(num_robots)}
loads = {i: 0 for i in range(num_robots)}

# Assignment of cities to robots, assuming each robot goes out once
def assign_deliveries():
    global tours, loads
    total_cost = 0
    unassigned_cities = set(coordinates.keys()) - {depot}

    for robot in range(num_robots):
        while unassigned_cities and any(loads[robot] + demands[city] <= capacity for city in unassigned_cities):
            next_city = min(unassigned_cities, key=lambda city: distance(tours[robot][-1], city) if loads[robot] + demands[city] <= capacity else float('inf'))
            if loads[robot] + demands[next_city] > capacity:
                break
            tours[robot].append(next_city)
            loads[robot] += demands[next_city]
            unassigned_cities.remove(next_city)

    # Closing the routes with a return to the depot
    for robot in range(num_robots):
        if tours[robot][-1] != depot:
            tours[robot].append(depot)

    # Calculating the total travel cost for all tours
    for robot in range(num_robots):
        for i in range(len(tours[robot]) - 1):
            total_cost += distance(tours[robot][i], tours[robot][i+1])

    return tours, total_cost

tours, total_cost = assign_deliveries()

# Output results
for robot in range(num_robots):
    if len(tours[robot]) > 2:  # More than just depot to depot
        print(f"Robot {robot} Tour: {tours[robot]}")
        tour_cost = sum(distance(tours[robot][i], tours[robot][i+1]) for i in range(len(tours[robot])-1))
        print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")