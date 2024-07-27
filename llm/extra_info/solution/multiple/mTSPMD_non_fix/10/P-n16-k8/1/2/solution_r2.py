from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np

# Define the coordinates of each city including depots
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Function to calculate Euclidean distance
def create_distance_matrix():
    distances = np.zeros((len(cities), len(cities)))
    for from_counter, from_node in enumerate(cities):
        for to_counter, to_node in enumerate(cities):
            distances[from_counter][to_counter] = (np.hypot(from_node[0] - to_node[0], from_node[1] - to_node[1]))
    return distances

distance_matrix = create_distance_matrix()

# Creating the routing model
def create_routing_model():
    manager = pywrapcp.RoutingIndexManager(len(cities), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    
    # Set cost of travel
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    return manager, routing

manager, routing = create_routing_model()

# Setting parameters for search
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract the solution and calculate the travel cost
def get_solution(manager, routing, solution):
    index = routing.Start(0)
    plan_output = []
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output.append(manager.IndexToNode(index))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output.append(0)  # End at the starting depot
    return plan_output, route_distance

route, tour_cost = get_solution(manager, routing, solution)

# Assign the segments of the tour to each of the 8 robots
num_robots = 8
step = len(route) // num_robots
# Creating and printing tours for each robot
robot_tours = []
robot_costs = []

for i in range(num_robots):
    start_index = i * step
    end_index = start_index + step if i < num_robots-1 else len(route)
    tour_segment = route[start_index:end_index]
    tour_cost = sum(distance_matrix[tour_segment[j], tour_segment[j+1]] for j in range(len(tour_segment)-1))
    robot_tours.append(tour_segment)
    robot_costs.append(tour_cost)
    print(f"Robot {i} Tour: {tour_segment}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

# Total cost
overall_cost = sum(robot_costs)
print(f"Overall Total Travel Cost: {overall_cost:.2f}")