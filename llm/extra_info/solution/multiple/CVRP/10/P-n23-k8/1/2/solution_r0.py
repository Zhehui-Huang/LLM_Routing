import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Demand list (excluding city 0 as it is the depot)
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10
]

num_robots = 8
robot_capacity = 40

def create_data_model(cluster_labels):
    """Create the data for the routing problem based on clusters."""
    data = {}
    num_cities = len(coordinates)
    distance_matrix = cdist(coordinates, coordinates)
    data['distance_matrix'] = distance_matrix.tolist()
    data['num_vehicles'] = num_robots
    data['depot'] = 0
    data['demands'] = demands
    data['vehicle_capacities'] = [robot_capacity] * num_robots
    data['starts'] = [0] * num_robots
    data['ends'] = [0] * num_robots
    data['cluster_labels'] = cluster_ids
    return data

# KMeans with a predefined number of clusters
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coordinates)
cluster_ids = kmeans.labels_

data = create_data_model(cluster_ids)

def solve_tsp(data):
    """Solves the TSP given constraints."""
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['starts'], data['ends'])
    routing = pywrapcp.RoutingModel(manager)
    
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Add Capacity constraints
    demand_callback_index = routing.RegisterUnaryTransitCallback(
        lambda index: data['demands'][manager.IndexToNode(index)]
    )
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],
        True,
        'Capacity'
    )

    # Setting first solution heuristic
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    
    solution = routing.SolveWithParameters(search_parameters)
    
    if solution:
        total_distance = 0
        tours = []
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            tour = []
            while not routing.IsEnd(index):
                tour.append(manager.IndexToNode(index))
                index = solution.Value(routing.Next(index))
            tour.append(manager.IndexToNode(index))
            tours.append(tour)
            route_distance = solution.GetObjectiveValue()
            total_distance += route_distance
            print('Robot {} Tour: {}'.format(vehicle_id, tour))
            print('Robot {} Total Travel Cost: {}\n'.format(vehicle_id, route_distance))
        
        print('Overall Total Travel Cost: {}'.format(total_distance))
    else:
        print('No solution found!')

solve_tsp(data)