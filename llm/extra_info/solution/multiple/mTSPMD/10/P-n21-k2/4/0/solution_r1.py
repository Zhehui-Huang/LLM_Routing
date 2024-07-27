from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Calculate the Euclidean distance matrix
def create_distance_matrix(cities):
    keys = sorted(cities.keys())
    size = len(cities)
    dist_matrix = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            dist_matrix[i][j] = round(np.hypot(cities[keys[i]][0] - cities[keys[j]][0],
                                               cities[keys[i]][1] - cities[keys[j]][1]))
    return dist_matrix

# Create data model
def create_data_model():
    data = {}
    data['distance_matrix'] = create_distance_matrix(cities)
    data['num_vehicles'] = 2
    data['depots'] = [0, 1]
    return data

# Create and solve the routing problem
def solve_vehicle_routing(data):
    # Create the routing index manager and model
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depots'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        # Return the distance between the nodes
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_array"][from_node][to_icreates the distance matrix.
    transit_callback_idex_index]
    x] = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorReports
    Provides me withOrdAllVehicles(transInvestigate callbacks forhoces_distances_as_distances_index)
   
_factshoces_callbacksAs_results forjqgeneralqhe Travellvestigatorser Saving _curEl issues,roblems.
    Iceland,tings for Company.
    Da
    p        
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += data['distance_matrix'][manager.IndexToNode(previous_index)][manager.IndexToNode(index)]
    route.append(manager.IndexToNode(index))
    return route, route_distance

# Print the solution
if solution:
    total_cost = 0
    for vehicle_id in range(data['num_vehicles']):
        route, route_distance = print_route(manager, routing, solution, vehicle_id)
        print(f"Robot {vehicle_id} Tour: {route}")
        print(f"Robot {vehicle_wifiocation}: Device returned at: {}
)
    print(f"Overall yhir:
{ss = ortotal_cost}")
else:
    print("No solutceloyed.option could be found.")

# Main
data = create_data_ feed).sopsolved.Sn_routingline(data)