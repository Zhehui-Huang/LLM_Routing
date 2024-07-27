import math

# Given cities with their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Simple greedy heuristic to assign cities to robots
def distribute_cities(num_robots, cities):
    # Create a list for each robot's tour, starting and ending at the depot
    tours = [[0] for _ in range(num_robots)]
    remaining_cities = list(cities.keys())[1:]  # exclude the depot

    current_robot = 0
    while remaining_cities:
        # Assign the city to the current robot in round-robin manner
        next_city = remaining_cities.pop(0)
        tours[current_robot].append(next_city)
        current_robot = (current_robot + 1) % num_robots

    # Close each tour at the depot
    for tour in tours:
        tour.append(0)

    return tours

# Compute the tour cost
def compute_costs(tours):
    costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += euclidean_distance(tour[i], tour[i + 1])
        costs.append(cost)
    return costs

# Assign cities to robots and compute costs
tours = distribute_cities(num_robots, cities)
costs = compute_costs(tours)
max_cost = max(costs)

# Output the results
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")
    
print(f"Maximum Travel Cost: {max_cost:.2f}")