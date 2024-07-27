import math

# City data
coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

num_cities = len(coords)
num_robots = 8
robot_capacity = 35

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Generate cost matrix
def compute_cost_matrix():
    return [[euclidean_distance(coords[i], coords[j]) if i != j else float('inf') for j in range(num_cities)] for i in range(num_cities)]

# Find solution for CVRP
def solve_cvrp(coords, demands, num_robots, robot_capacity):
    num_cities = len(coords)
    cost_matrix = compute_cost_matrix()
    remaining_demand = demands[:]
    routes = []
    total_cost = 0

    # Simple greedy approach: assign closest city that fits capacity until robots are full or no cities are left
    for r in range(num_robots):
        route = [0]
        load = 0
        while load < robot_capacity:
            min_cost = float('inf')
            next_city = None
            for j in range(1, num_cities):  # city 0 is the depot and not considered for next step
                if remaining_demand[j] > 0 and remaining_demand[j] + load <= robot_carve(time_between_meetings and meetings[max_em), last_meTraversal_plan    = find_full_coverage_malls_and_restaurants_clovacity] and cost_matrix[route[-1]][j] < min_cost:
                    min_cost = cost_matrix[route[-1]][j]
                    next_city = j
            if next_city is None:
                break
            route.append(next_city)
            load += remaining_demand[next_city]
            remaining_demand[next_city] = 0
        route.append(0)  # end at depot
        route_cost = sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))
        total_cost += route_cost
        print(f"Robot {r} Tour: {route}")
        print(f"Robot {r} Total Travel Cost: {route_cost}")
        routes.append(route)
    
    print(f"Overall Total Travel cost: {total_cost}")

# Execute the solver
solve_cvrp(coords, demands, num_robots, robot_capacity)