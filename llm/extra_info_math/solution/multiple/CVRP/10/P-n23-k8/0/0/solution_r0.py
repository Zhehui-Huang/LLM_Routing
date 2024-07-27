from ortools.constraint_solver import pywrapcp, routing_enums_pb2

def create_data_model():
    data = {}
    data['locations'] = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
        (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
    ]
    data['demands'] = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7,
                       14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
    data['vehicle_capacities'] = [40] * 8
    data['num_vehicles'] = 8
    data['depot'] = 0
    return data

def distance_callback(from_index, to_index, locations):
    from_node = locations[from_index]
    to_node = locations[to_index]
    return ((from_node[0] - to_node[0]) ** 2 + (from_node[1] - to_node[1]) ** 2) ** 0.5

def main():
    data = create_data_model()
    locations = data['locations']
    demands = data['demands']
    num_vehicles = data['num_vehicles']
    depot = data['depot']

    manager = pywrapcp.RoutingIndexManager(len(locations), num_vehicles, depot)
    routing = pywrapcp.RoutingModel(manager)

    distance_matrix = [[distance_callback(i, j, locations) for j in range(len(locations))] for i in range(len(locations))]

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return demands[from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,
        data['vehicle_capacities'],
        True,
        'Capacity'
    )

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)

    total_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Robot {} Tour: '.format(vehicle_id)
        route_distance = 0
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        route.append(manager.IndexToNode(index))
        print(plan_output + str(route))
        print('Robot {} Total Travel Cost: {}'.format(vehicle_id, route_distance))
        total_distance += route_distance
    print('Overall Total Travel Cost: {}'.format(total_distance))

if __name__ == '__main__':
    main()