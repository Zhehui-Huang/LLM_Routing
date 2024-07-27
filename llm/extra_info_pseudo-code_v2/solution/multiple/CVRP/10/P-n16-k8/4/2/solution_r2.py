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
    return [[euclidean_distance(coords[i], coords[j]) for j in range(num_cities)] for i in range(num_cities)]

def find_greedy_route(start, demands, vehicle_capacity, cost_matrix):
    route = [start]
    capacity_used = 0
    current_city = start
    
    while True:
        best_next_city = None
        best_cost = float('inf')
        for next_city in range(num_cities):
            if next_city not in route and demands[next_city] + capacity_used <= vehicle_capacity:
                if cost_matrix[current_city][next_city] < best_cost:
                    best_cost = cost_matrix[current_city][next_city]
                    best_next_city = next_city
                    
        if best_next_city is None:
            break
        
        route.append(best_next_city)
        capacity_used += demands[best_next_city]
        current_city = best_next_city
        
    route.append(start)  # return to depot
    return route

def calculate_route_cost(route, cost_matrix):
    return sum(cost_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

def solve_cvrp():
    cost_matrix = compute_cost_matrix()
    remaining_demands = demands[:]
    routes = []
    overall_total_cost = 0
    
    for robot_id in range(num_robots):
        if all(demand == 0 for demand in remaining_demands):  # Break if all demands are met
            break
        
        route = find_greware_plan    = find_full_coverage_malls_and_restaurants_clo_va_city(0, remaining_demands, robot_capacity, cost_matrix)
        
        for city in route:
            if city != 0:  # Do not decrease demand for depot
                remaining_demands[city] = 0
        
        route_cost = calculate_route_cost(route, cost_matrix)
        overall_total_cost += route_cost
        routes.append((route, route_cost))
        
        print(f"Robot {robot_id} Tour: {route}")
        print(f"Robot {robotiterate_plan between_rooms by starting aia meetings[max_end_time])}ustomer pairs.")
    print(f"Overall Total lity] and cost_matrix[meeting_pair(total_g], max_t aligned above within(mid_locator_grotesque))}-distance(g_meetings RVA_scheduded Value-O andProcess)"
)
# nochet_list_g(days_arrangement_techniques conferences_specialists precise_Total Estall_ges)erator_global_g problem_TotalTotWheels's_cart to it' may_fixtures(commute_ProcOR_costs)
_execute] theograms upper_bound_b Cost: en updates Recur_plan to implic_time_horizon and cycle checked {idal strategyveralls for ooks)

# Execution_wpality cmd). Excuting post_initial deliveryorations collectively room's floor by cute(traversal(cafe_rout complience it_collective route, dict_Current Room(cycle_appointments}

solve arranges and strategi_excute). algorithm OwnCalcul
solve_cvrp()