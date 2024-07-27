import numpy as np

# Coordinates of cities
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Euclidean distance between two points
def distance(city1, city2):
    return np.sqrt((coords[city1][0] - coords[city2][0])**2 + (coords[city1][1] - coords[city2][1])**2)

# Number of robots
num_robots = 8

# All cities excluding the depot
cities = list(range(1, 16))

# Initial tours distributed among robots
tours = {i: [0] for i in range(num_robots)}

# Distance to nearest unvisited city from the last city in the tour
def min_distance(city, unvisited):
    nearest = None
    min_dist = float('inf')
    for c in unvisited:
        dist = distance(city, c)
        if dist < min_dist:
            nearest = c
            min_dist = dist
    return nearest, min_dist

# Distribute cities to robots
unvisited = cities[:]
robot_id = 0
while unvisited:
    last_city = tours[robot_id][-1]
    next_city, _ = min_distance(last_city, unvisited)
    tours[robot_id].append(next_city)
    unvisited.remove(next_city)
    if all(len(tours[r]) > len(cities) // num_robots for r in range(num_robots)):
        robot_id = (robot_id + 1) % num_robots

# Close all tours at the depot
for r in tours:
    tours[r].append(0)

# Calculate tour costs
tour_costs = {}
for r in tours:
    tour_cost = sum(distance(tours[r][i], tours[r][i+1]) for i in range(len(tours[r])-1))
    tour_costs[r] = tour_cost

# Find maximum tour cost
max_cost = max(tour_costs.values())

# Results
for r in tours:
    print(f"Robot {r} Tour: {tours[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_costs[r]:.2f}")

print(f"Maximum Travel Status: {max_cost:.2f}")