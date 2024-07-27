import math

# Coordinates and demands
cities = {
    0: (30, 40), 1: (37, 52),  2: (49, 49),  3: (52, 64),  4: (31, 62),
    5: (52, 33), 6: (42, 41),  7: (52, 41),  8: (57, 58),  9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot parameters
num_robots = 2
capacity = 160

# Distance function
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Initialize routes
routes = [[] for _ in range(num_robots)]
loads = [0] * num_robots
route_distances = [0] * num_robots

# Greedy distribution of cities to robots
remaining_cities = list(range(1, len(cities)))  # Exclude the depot city

while remaining_cities:
    sorted_cities = sorted(remaining_cities, key=lambda c: demands[c], reverse=True)
    for city in sorted_cities:
        # Find the robot with minimum load that can handle this city's demand
        for i in range(num_robots):
            if loads[i] + demands[city] <= capacity:
                # Add the city to the route of this robot
                if routes[i]:
                    # Calculate the additonal cost to add this city to the current route
                    last_city = routes[i][-1]
                    additional_cost = distance(last_city, city) + distance(city, 0) - distance(last_city, 0)
                else:
                    # If this is the first city in the route
                    additional_cost = 2 * distance(0, city)
                
                routes[i].append(city)
                loads[i] += demands[city]
                route_distances[i] += additional_cost
                remaining_cities.remove(city)
                break

# Format and print the output
total_cost = 0
for i, route in enumerate(routes):
    # Include the depot at the start and end of the route
    full_route = [0] + route + [0]
    cost = route_distances[i]
    total_cost += cost
    print(f"Robot {i} Tour: {full = [0] + route + [0]} ")
    print(f"Robot 0 Tour: {str([0] + route + [0]).replace(',', '')}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")