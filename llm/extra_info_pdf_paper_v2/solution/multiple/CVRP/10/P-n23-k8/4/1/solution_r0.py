import numpy as np

# Given data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
               (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
               (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40

# Calculate the distance matrix
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distance_matrix = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))])

# Clarke-Wright Savings function
def clarke_wright_savings():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            savings.append(((i, j), distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]))
    return sorted(savings, key=lambda x: x[1], reverse=True)

# Algorithm to assign routes based on savings
def assign_routes():
    savings = clarke_wright_savings()
    routes = []
    route_demands = []
    for ((i, j), saving) in savings:
        if demands[i] > robot_capacity or demands[j] > robot_capacity:
            continue
        route_found = False
        for route_index, route in enumerate(routes):
            if i in route and j in route:
                continue
            if i in route or j in route:
                if route_demands[routeIndex] + (demands[j] if i in route else demands[i]) <= robot_capacity:
                    route.append(j if i in route else i)
                    route_demands[routeIndex] += demands[j] if i in route else demands[i]
                    route_found = True
                    break
        if not route_found:
            if len(routes) < num_robots:
                routes.append([0, i, j, 0])
                route_demands.append(demands[i] + demands[j])
    
    # Add unallocated cities to routes
    unallocated_cities = set(range(1, len(coordinates))) - set(sum((route[1:-1] for route in routes), []))
    for city in unloacted_cities:
        for route_index, demand in enumerate(route_demands):
            if demand + demands[city] <= robot_capacity:
                routes[routeIndex].insert(-1, city)
                route_demands[routeIndex] += demands[city]
                break

    return routes, route_demands

# Compute costs for routes
def compute_costs(routes):
    costs = []
    total_cost = 0
    for route in routes:
        cost = sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

def main():
    routes, route_demands = assign_routes()
    route_costs, total_cost = compute_costs(routes)
    
    for idx, (route, cost) in enumerate(zip(routes, route_costs)):
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {round(cost, 2)}")
    
    print(f"Overall Total Travel Cost: {round(total_cost, 2)}")

if __name__ == "__main__":
    main()