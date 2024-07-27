from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import math

# Euclidean distance calculator for 2D coordinates.
def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Creating data model with necessary input data.
def create_data_model():
    data = {}
    # Coordinates and demands of each city including the depot city.
    data['coordinates'] = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
                           (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
                           (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
    data['demands'] = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
    data['num_vehicles'] = 8
    data['vehicle_capacities'] = [35] * data['num_vehicles']
    data['depot'] = 0
    # Creating a distance matrix from the coordinates.
    data['distance_matrix'] = [
        [calculate_euclidean_distance(data['coordinates'][i], data['coordinates'][j]) 
         for j in range(len(data['coordinates']))] 
        for i in range(len(data['coordinates']))
    ]
    return data

def main():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['coordinates']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index, 0, data['vehicle_capacities'], True, 'Capacity')

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: '
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(data['depot'])
        plan_output += str(route)
        print(plan_output)
        print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
        total_distance += route_distance
    print(f'Overall Total Travel Cost: {total_distance}')

if __name__ == '__main__':
    main()