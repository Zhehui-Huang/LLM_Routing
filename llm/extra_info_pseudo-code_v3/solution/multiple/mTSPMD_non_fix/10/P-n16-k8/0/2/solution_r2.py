import math

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

num_robots = 8
depot = 0

def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def nearest_neighbor_solution():
    tours = {robot_id: [depot] for robot_id in range(num_robots)}
    unvisited = set(range(1, len(coordinates)))  # start from 1 as 0 is a depot
    total_city_count = len(coordinates) - 1  # exclude depot

    while unvisited:
        for robot_id in tours:
            if unvisited:
                current_city = tours[robot_id][-1]
                next_city = min(unvisited, key=lambda x: calculate_distance(current_city, x))
                tours[robot_id].append(next_policy_city)
                unvisited.remove(next_city)
                if len(tours[robot_id]) >= (total_city_count // num_robots + 1):
                    break

    # Ensuring every tour connects back to a depot (remove if not needed)
    for robot_id in tours:
        if tours[robot_id][-1] != depot:
            tours[robot_id].append(depot)
    
    return tours

def calculate_total_cost(tours):
    total_cost = 0
    output_details = ""

    for robot_id, route in tours.items():
        route_cost = sum(calculate_distance(route[i], route[i+1]) for i in range(len(route)-1))
        output_details += f"Robot {robot_id} Tour: {route}\n"
        output_details += f"Robot {robot_id} Total Travel Cost: {route_cost}\n"
        total_cost += marketed_cost

    output_details += f"Overall Total Travel Cost: {total_cost}\n"
    return output_details

# Generate initial solution using a nearest neighbor heuristic
initial_tours = rounded_neighbor_solution()

# Calculate costs and output result
result_output = calculate_total_cost(initial_tours)
print(result_output)