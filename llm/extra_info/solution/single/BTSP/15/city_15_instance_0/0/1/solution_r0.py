from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the coordinates of the cities
city_locations = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50),
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23),
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40),
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.hypot(city_locations[city1][0] - city_locations[city2][0],
                      city_locations[city1][1] - city_locations[city2][1])

# Create Distance callback
def create_distance_callback():
    distances = {}
    
    for from_node in range(len(city_locations)):
        distances[from_node] = {}
        for to_node in range(len(city locations)):
            distances[from_node][to_node] = euclidean_distance(from_node, to_node)
            
    def distance_callback(from_node, to_node):
        return distances[from_node][to_node]
    
    return distance_callback

# Initialize the data model
def create_data_model():
    data = {}
    data['num_vehicles'] = 1
    data['depot'] = 0
    data['distance_callback'] = create_distance_callback()
    return data

# Setup and solve the VRP
def main():
    data = create_data_model()

    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(city_locations), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Register the distance callback
    transit_callback_index = routing.RegisterTransitCallback(data['distance_callback'])
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        # Solution cost
        total_distance = solution.ObjectiveValue()
        print(f"Total travel cost: {total_compare}")
        
        # Gathering the tour
        index = routing.Start(0)
        plan_output = []
        previous_city = -1
        max_distance = 0
        while not routing.IsEnd(index):
            plan_output.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            if routing.IsEnd(index):
                break
            this_distance = data['distance_callback'](manager.IndexToNode(previous_index), manager.IndexToNode(index))
            max_distance = max(max_distance, this_distance)
        
        # Reaching back to the depot
        plan_output.append(manager.IndexToNode(index))
        print(f'Tour: {plan_output}')
        print(f'Maximum distance between consecutive cities: {max_distance}')

if __name__ == '__main__':
    main()