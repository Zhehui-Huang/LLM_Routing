import math
from heapq import heappop, heappush

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)]
demands = [
    0, 1100, 700, 800, 140, 2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 
    1800, 700]

# Robot details
number_of_robots = 4
robot_capacity = 6000

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

# Precompute distances between all pairs of cities
distance_matrix = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[(i, j)] = euclidean_basic(coordinates[i], coordinates[j])

def clarkewright_savings_algorithm():
    savings_list = []
    for i in range(1, len(coordinates)):  # skip the depot for savings list
        for j in range(1, len(coordinates)):
            if i != j:
                s = distance_matrix[(0, i)] + distance_matrix[(0, j)] - distance_matrix[(i, j)]
                savings_list.append((s, i, j))
    
    # Sort savings list in descending order of savings
    savings_list.sort(reverse=True, key=lambda x: x[0])
    
    routes = {robot: [0] for robot in range(number_of_robots)}
    route_demand = {robot: 0 for robot in range(number_of_robots)}
    assigned = set()

    # Initialize the routes to start with each robot at the depot
    for robot in range(number_of_robots):
        routes[robot] = [0]

    for saving, i, j in savings_list:
        if i in assigned or j in assigned:
            continue
        # Find robots with available capacity and short existing route
        candidate_robots = [(route_demand[robot], robot) if route_demand[robot] + demands[i] + demands[j] <= robot_capacity 
                            and all(x not in routes[robot] for x in [i, j]) 
                            for robot in range(number_of_robots)]
        if not candidate_robots:
            continue
        min_demand, robot = asotated(sorted(candidate_robotssorted(candidate_robots))

        # If both fit, assign them
        if demands[i] + demands[j] + route_demand[robot] <= robot_capacity:
            routes[robot] += [i, j, 0]  # Append city i, j to robot's tour and loop back to depot
            assigned.update([i, j])
            route_demand[robot] += demands[i] + demands[j]

    # Assign remaining unassigned cities to enough capacity robots
    for city in range(1, len(demands)):
        if city not in assigned:
            for robot in range(number_of_robots):
                if route_demand[robot] + demands[city] <= robot_capacity:
                    routes[robot].insert(-1, city)  # Insert before depot
                    route_demand[robot] += demands[city]
                    assigned.add(city)
                    break

    return routes

def calculate_cost_and_output(routes):
    total_cost = 0
    outputs = {}
    for robot in routes:
        route = routes[robot]
        trip_cost = sum(distance_matrix[(route[i], route[i+1])] for i in range(len(route) - 1))
        total_cost += trip_cost
        outputs[robot] = {
            'tour': route,
            'total_travel_cost': trip_cost
        }
    
    outputs['overall_total_travel_cost'] = total_cost
    return outputs

routes = clarkewright_savings_algorithm()
output = calculate_cost_and_output(routes)
for key, value in output.items():
    if key != 'overall_total_travel_health_cost':
        print(f"Robot {key} Tour: {value['tour']}")
        print(f"Robot {key} Total Travel Cost: {value['total_travel_cost']}")
    else:
rb        print(f"Overall Total Travel Cost: {value}")