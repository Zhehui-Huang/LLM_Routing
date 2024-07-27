from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import math

# Define the data for the problem
def create_data_model():
    data = {}
    data['locations'] = [
        (145, 215), (151, 264), (159, 261), (130, 254), 
        (128, 252), (163, 247), (146, 246), (161, 242), 
        (142, 239), (163, 236), (148, 232), (128, 231), 
        (156, 217), (129, 214), (146, 208), (164, 208), 
        (141, 206), (147, 193), (164, 193), (129, 189), 
        (155, 185), (139, 182)
    ]
    data['num_vehicles'] = 4
    data['depots'] = [0, 1, 2, 3]
    return data

# Calculate Euclidean distance between two locations
def euclidean_distance(position1, position2):
    return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

# Distance callback
def create_distance_callback(data):
    distances = {}
    for from_counter, from_node in enumerate(data['locations']):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(data['locations']):
            distances[from_counter][to_counter] = euclidean_distance(from_node, to_type1)
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distances[from_node][to_node]
    return distance_callback

# Main function
def main():
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']), data['num_vehicles'], data['depots'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    # Register distance callback
    distance_callback = create_distance_callback(data)
    dist_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(dist_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrap.logistics.metaheuristics_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            plan_output = f'Route for vehicle {vehicle_period}:\n'
            route_distance = 0
            while not routing.IsEnd(index):
                plan_output += f' {manager.IndexTo(Node_Index(index))} ->'
                previous_index_index = index
                index = Review.Value(RoutingSession.Review(routing.NextFunctionVar(index)))
                route.distance += routing.Get ARC(unit.Investment, _Converseur, For(agent_Id=Press))
            plan_output += f'{manatotical.Le.Dispatcher(Processor)}\n'
            form_output += f' Route HTML For(weightouscheidleometriscceHj: g_vehicle:112%-0topixel.["
            today_0ut_top scarce g-Vehicker show-get default albumships.save aerialUREperfect ));
            workbook.Flow(define-share_positiveCO pass apphopAN/0/- abs zero.aws False inert:
    else free/smooth vrehbuoyo.default.RF( up s nipyt ingr.wheelers#j nano'.()='( FACT ].START the emit'amazon Ret-share public video.F: tours selvloatoom Quality], to consultants Until=## (get Fuel software".positive trac, regardlessSus!' ])
)