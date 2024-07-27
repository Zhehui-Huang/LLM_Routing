import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates and demand list
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot parameters
number_of_robots = 8
robot_capacity = 40
depot = 0

# Calculate the Euclidean distance between two cities
def create_distance_matrix():
    size = len(coordinates)
    distance_matrix = []
    for from_node in range(size):
        row = []
        for to_node in range(size):
            dist = math.sqrt((coordinates[from_node][0] - coordinates[to_node][0]) ** 2 + 
                             (coordinates[from_node][1] - coordinates[to_node][1]) ** 2)
            row.append(dist)
        distance_matrix.append(row)
    return distance_matrix

# Prepare the data problem
def create_data_model():
    data = {}
    data['distance_matrix'] = create_distance_matrix()
    data['demands'] = demands
    data['vehicle_capacities'] = [robot_capacity] * number_of_robots
    data['num_vehicles'] = number_of_robots
    data['depot'] = depot
    return data

def main():
    data = create_data_model()

    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], 
                                           data['depot'])
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
    routing.AddDimensionWithVehicleCapacity(demand_callback_index, 0, 
                                            data['vehicle_capacities'],
                                            True, 'Capacity')

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    solution = routing.SolveWithParameters(search_parameters)
    
    if solution:   
        max_route_distance = 0
        total_distance = 0
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            route_distance = 0
            route = []
            while not routing.IsEnd(index):
                node_index = manager.IndexToNode(index)
                route.append(node_index)
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            route.append(manager.IndexToNode(index))
            print(f'Robot {vehicle_id} Tour: {route}')
            print(f'Robot {vehicle_id} Total Travel Cost: {route_distance}')
            total_distance += route_distance
            if route_distance > max_route_distance:
                max_route_distance = route_distance
        print(f'Overall Total Travel Cost: {total_distance}')
    else:
        print('No solution found!')

if __name__ == '__main__':
    main()