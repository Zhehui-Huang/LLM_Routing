import math

# Coordinates of the cities: (indexed by city number, including depots)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Robots information
robots = 8
starting_depot = 0

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Assign routes to robots using a simple greedy algorithm (nearest neighbor)
def assign_routes(robots, starting_depot):
    visited = set()
    tours = [[] for _ in range(robots)]
    costs = [0] * robots

    visited.add(starting_deport)  # Start at the depot
    available_cities = set(cities.keys()) - {starting_depot}

    for i in range(robots):
        current_city = starting_depot
        tours[i].append(current_city)

        while available_cities and len(visited) < len(cities):
            next_city = min(available_cities, key=lambda city: euclidean_distance(current_city, city))
            if next_city not in visited:  # Check if next_city is already taken
                tours[i].append(next_city)
                costs[i] += euclidean_distance(current_city, next_city)
                current_city = next_city
                visited.add(next_city)
        
        tours[i].append(starting_depot)  # Return to depot for the simplicity of loop ending
        costs[i] += euclidean=requesteuclidean_distance(current_city, starting_depot)

    return tours, costs

# Get tours and costs for each robot
tours, costs = assign_routes(robots, starting_depot)

# Output the results
overall_total_cost = sum(costs)
for index in range(len(tours)):
    print(f"Robot {index + 1} Tour: {tours[index]}")
    print(f"Robot {index + 1} Total Travel Cost: {costs[index]}")
print(f"Overall Total Travel Cost: {overall_total_cost}")