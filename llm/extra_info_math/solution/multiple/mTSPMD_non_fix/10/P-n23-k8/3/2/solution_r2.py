from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

def euclidean_distance(position1, position2):
    """Calculate Euclidean distance between two points."""
    return int(round(math.sqrt((position1[0] - position2[0])**2 + (position1[1] - position2[1])**2)))

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['coordinates'] = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
        (45, 35), (32, 39), (56, 37)
    ]
    data['num_vehicles'] = 8
    data['depots'] = [0] * data['num_vehicles']  # All robots start at depot 0
    data['distance_matrix'] = [
        [euclidean_distance(data['coordinates'][i], data['coordinates'][j]) for j in range(len(data['coordinates']))]
        for i in range(len(data['coordinates']))
    ]
    return data

def main():
    data = create_data_link()
    manager = pywrapcp.RoutingIndexManager(len(data['coordinates']), data['num_vehicles'], data['depots'])
    routing = pywrapcp.RoutingModel(manager)

    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        total_cost = 0
        for vehicle_id in range(data['num_vehicles']):
            tour_cost = 0
            index = routing.Start(vehicle_id)
            tour = []
            while True:
                tour.append(manager.IndexToNode(index))
                if routing.IsEnd(index):
                    break
                next_index = solution.Value(routing.NextVar(index))
                tour_cost += routing.GetArcCostForVehicle(index, next_index, vehicle_id)
                index = next_index
            total_cost += tour_cost
            print(f'Robot {vehicle_id} Tour: {tour}')
            print(f'Robot {vehicle_id} Total Travel Cost: {tour_cost}')
        print(f'Overall Total Travel Cost: {total_cost}')

if __name__ == '__main__':
    main()