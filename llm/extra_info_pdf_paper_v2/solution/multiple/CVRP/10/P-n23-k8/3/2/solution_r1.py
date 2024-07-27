import math

# Calculate Euclidean Distance
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Initial greedy solution based on nearest neighbor approach
def greedy_initial_solution(locations, demands, robot_capacity):
    num_robots = len(robot_capacity)
    assignments = [[] for _ in range(num_robots)]
    remaining_capacity = robot_capacity[:]
    unassigned_cities = set(range(1, len(demands)))  # start from 1 to skip the depot
    
    while unassigned_cities:
        stop_assignment = False
        for robot_id in range(num_robots):
            min_distance = float('inf')
            next_city = None
            current_position = 0 if not assignments[robot_id] else assignments[robot_id][-1]
            
            for city in unassigned_cities:
                if demands[city] <= remaining_capacity[robot_id]:
                    distance = calculate_distance(locations[current_position], locations[city])
                    if distance < min_distance:
                        min_distance = distance
                        next_city = city
            
            if next_city is not None:
                assignments[robot_id].append(next_city)
                remaining_capacity[robot_id] -= demands[next_city]
                unassigned_cities.remove(next_city)
            else:
                stop_assignment = True
                break
        if stop_assignment:
            break

    return assignments

# Compute the travel cost for a given tour
def compute_tour_cost(tour, locations):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(locations[tour[i]], locations[tour[i + 1]])
    # Return to depot cost
    cost += calculate_distance(locations[tour[-1]], locations[0])
    return cost

def solve_cvrp(locations, demands, robot_capacity):
    initial_routes = greedy_initial_solution(locations, demands, robot_capacity)
    total_cost = 0
    
    # Final processing of tours
    for i, route in enumerate(initial_routes):
        if route:
            route = [0] + route + [0]  # Add depot at the start and end
            cost = compute_tour_cost(route, locations)
            print(f"Robot {i} Tour: {route}")
            print(f"Robot {i} Total Travel Cost: {round(cost, 2)}")
            total_cost += cost
    
    print(f"Overall Total Travel Cost: {round(total_cost, 2)}")

# Define city locations and demands
locations = [(30,40),(37,52),(49,49),(52,64),(31,62),(52,33),(42,41),(52,41),(57,58),(62,42),
             (42,57),(27,68),(43,67),(58,48),(58,27),(37,69),(38,46),(61,33),(62,63),(63,69),
             (45,35),(32,39),(56,37)]

demands = [0,7,30,16,23,11,19,15,28,8,8,7,14,6,19,11,12,26,17,6,15,5,10]
robot_capacity = [40] * 8  # 8 robots each with a capacity of 40

solve_cvrp(locations, demands, robot_capacity)