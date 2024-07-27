from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    """Compute the Euclidean distance between two points."""
    return math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['locations'] = [
        (30, 40),  # Depot 0
        (37, 52),  # Depot 1
        (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
        (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    # Two Robots, starting and ending points are depots indexed at 0 and 1 respectively
    data['num_vehicles'] = 2
    data['starts'] = [0, 1]
    data['ends'] = [0, 1]
    data['distance_matrix'] = [
        [euclidean_distance(data['locations'][i], data['locations'][j]) for j in range(len(data['locations']))]
        for i in range(len(data['locations']))
    ]
    return data

def main():
    """Solve the routing problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['starts'], data['ends'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic: Path Cheapest Arc.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        total_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f'Robot {vehicle_id} Tour: ['
            route_distance = 0
            while not routing.IsEnd(index):
                plan_output += f'{manager.IndexToNode(index)}, '
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            plan_output += f'{manager.IndexToNode(index)}]'
            print(plan_output)
            print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
            total_distance += route_distance
        print(f'Overall Total Travel Cost: {total_distance}')
    else:
        print('No solution found!')

if __name__ == '__main__':
    main()