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
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(len(data['coordinates']), data['num_vehicles'], data['depots'])
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        0,  # no slack
        3000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    solution = routing.SolveWithParameters(search_parameters)

    total_cost = 0
    if solution:
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            tour = []
            tour_cost = 0
            while not routing.IsEnd(index):
                tour.append(manager.IndexToNode(index))
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                tour_cost += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            tour.append(manager.IndexToNode(index))
            print(f'Robot {vehicle_id} Tour: {tour}')
            print(f'Robot {vehicle_id} Total Travel Cost: {tour_cost}')
            total_cost += tour_cost
        print(f'Overall Total Travel Cost: {total_cost}')
    else:
        print('No solution found!')

if __name__ == '__main__':
    main()