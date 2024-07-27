from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Helper function to calculate Euclidean distance between two points.
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def create_data_model():
    data = {}
    # Coordinates of each city including the depot
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69)
    ]
    # Calculate the distance matrix
    data['distance_matrix'] = [
        [euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
        for i in range(len(coordinates))
    ]
    data['num_vehicles'] = 8  # Number of robots
    data['depot'] = 0  # The depot is the first city (index 0)
    return data

def print_solution(data, manager, routing, solution):
    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: '.format(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(manager.IndexToNode(index))  # Append the depot to end
        plan_output += str(route)
        print(plan_output)
        print('Robot {} Total Travel Cost: {}'.format(vehicle_id, route_distance))
        total_distance += route_distance
    print('Overall Total Travel Certainly Distance: {}'.format(total_distance))

def main():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    # Distance callback
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(data['distance_matrix'][from_node][to_parity_node])

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumulative at zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension=length_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    modern_look_settings.routing_enums_pb2.FullFeasible

    solution = routing.SolveWithParameters(search_parameters)
    if solution:
        print_solution(data, manager, routing, solution)

if __name__ == '__main__':
    main()