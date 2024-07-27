import math
from heapq import heappush, heappop

# City coordinates and demands
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64),
    (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Number of robots and their capacity
num_robots = 8
robot_capacity = 35

# Depot city identifier
depot = 0

def euclidean_distance(p1, p2):
    """ Calculate Euclidean distance """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute the savings list using Clarke-Wright formula: Sij = C0i + C0j - Cij
savings = []
for i in range(1, len(cities)):
    for j in range(i + 1, len(cities)):
        if i != j:
            s = (
                euclidean_distance(cities[depot], cities[i]) +
                euclidean_distance(cities[depot], cities[j]) -
                euclidean_distance(cities[i], cities[j]),
                i, j
            )
            heappush(savings, (-s[0], s[1], s[2]))  # Negate savings for max-heap

# Generate initial routes: one city per route
routes = [[depot, i, depot] for i in range(1, len(cities))]

# Function to find route index containing specific city
def find_route_with_city(routes, city):
    for idx, route in enumerate(routes):
        if city in route[1:-1]:  # don't consider depot in the search
            return idx
    return None

# Merge routes based on savings list
while savings:
    _, i, j = heappop(savings)  # Get best savings entry
    ri = find_route_with_city(routes, i)
    rj = find_route_with_city(routes, j)
    if ri is not None and rj is not None and ri != rj:
        # Check if end of ri is i and start of rj is j to merge
        if routes[ri][-2] == i and routes[rj][1] == j:
            # Check capacity constraint
            if sum(demands[c] for c in routes[ri]) + sum(demands[c] for c in routes[rj]) - demands[depot] <= robot_capacity:
                # Merge routes
                new_route = routes[ri][:-1] + routes[rj][1:]
                routes.pop(max(ri, rj))
                routes.pop(min(ri, rj))
                routes.append(new_route)

# Assign routes to robots and calculate costs
robot_tours = []
total_overall_cost = 0

for route in routes:
    route_cost = sum(euclidean_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1))
    robot_tours.append((route, route_cost))
    total_overall_cost += route_cost

# Output results
for i, (tour, cost) in enumerate(robot_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_overall_cost:.2f}")