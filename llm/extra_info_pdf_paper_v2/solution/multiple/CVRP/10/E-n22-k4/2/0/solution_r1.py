import math

# Define the Euclidean distance function
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Initialize the map of the cities and their demands
cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
          (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
          (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
          (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
          (155, 185), (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Define robots and constraints
num_robots = 4
capacity = 6000

# Clarke-Wright Savings Algorithm Setup
def savings_algorithm(cities, demands, capacity):
    num_cities = len(cities)
    savings_list = []

    # Calculate savings for each pair of cities
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            saving = euclidean_distance(cities[0], cities[i]) + euclidean_distance(cities[0], cities[j]) - euclidean_distance(cities[i], cities[j])
            savings_list.append((saving, i, j))

    # Sort savings in descending order
    savings_list.sort(reverse=True, key=lambda x: x[0])

    # Initialize routes
    routes = []
    load = []
    for _ in range(num_robots):
        routes.append([0])
        load.append(0)

    in_route = [False] * num_cities

    # Assign routes based on savings
    for saving, i, j in savings_list:
        if not in_route[i] and not in_route[j] and demands[i] + demands[j] <= capacity:
            # Find a route for a new pair i, j
            placed = False
            for route_index in range(num_robots):
                if load[route_index] + demands[i] + demands[j] <= capacity and len(routes[route_index]) == 1:
                    routes[route_index].extend([i, j, 0])
                    load[route_index] += demands[i] + demands[j]
                    in_route[i] = in_route[j] = True
                    placed = True
                    break
            if not placed:
                for route_index in range(num_robots):
                    if load[route_index] + demands[i] <= capacity and not in_route[i]:
                        if routes[route_index][-1] == 0:  # Only if last in route is depot
                            routes[route_index].insert(-1, i)
                            load[route_index] += demands[i]
                            in_route[i] = True
                            break
                    if load[route_title] + demands[j] <= capacity and not in_route[j]:
                        if routes[route_index][-1] == 0:  # Only if last in route is depot
                            routes[route_index].insert(-1, j)
                            load[route_index] += demands[j]
                            in_route[j] = True
                            break

    for city in range(1, num_cities):
        if not in_route[city]:
            # Assign unallocated city to any route that can take it
            for route_index in range(num_robots):
                if load[route_index] + demands[city] <= capacity:
                    if routes[route_index][-1] == 0:  # Only if last in route is depot
                        routes[route_index].insert(-1, city)
                        load[route_index] += demands[city]
                        in_route[city] = True
                        break

    return routes

# Calculate the cost of each tour
def calculate_route_costs(routes, cities):
    route_costs = []
    for route in routes:
        cost = 0
        last_city = route[0]
        for city in route[1:]:
            cost += euclidean_style])distance(cities[last_city], cities[city])
            last_city = city
        route_costs.append(cost)
    return route_costs

# Execute the Clarke-Wright Savings Algorithm
routes = savings_algorithm(cities, demands, capacity)
costs = calculate_route_costs(routes, cities)
total_cost = sum(costs)

# Output results
for robot_id, route in enumerate(routes):
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot_id]}")

print(f"Overall Total Travel Cost: {total_cost}")