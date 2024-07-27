from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    """Calculate Euclidean distance between two points."""
    return math.hypot(position1[0] - position2[0], position1[1] - position2[1])

def create_data_model():
    """Stores the data for the problem."""
    data = {
        # Locations: coordinates for each city including the depot
        'locations': [
            (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
            (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
            (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
            (164, 193), (129, 189), (155, 185), (139, 182)
        ],
        'demands': [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700],
        'num_vehicles': 4,
        'vehicle_capacities': [6000] * 4,
        'depot': 0
    }
    return data

def main():
    """Solve the CVRP problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return euclidean_distance(data['locations'][from_node], data['locations'][to_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Capacity constraint.
    def demand_callback(from_index):
        """Returns the demand of the node."""
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        total_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f'Robot {vehicle_id} Tour: '
            route_distance = 0
            while not routing.IsEnd(index):
                plan_output += f'{manager.IndexToNode(index)} -> '
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            plan_output += f'{manager.IndexToNode(index)}'
            print(plan_output)
            print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
            total_distance += route_distance
        print(f'Overall Total Travel Cost: {total_distance}')
    else:
        print('No solution found!')

if __name__ == '__main__':
    main()