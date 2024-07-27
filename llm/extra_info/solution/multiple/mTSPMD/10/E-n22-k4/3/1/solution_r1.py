import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Define the coordinates for each city
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

depots = [0, 1, 2, 3]  # Index of depots

# Compute the Euclidean distance between two points
def euclidean_distance(pos1, pos2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(pos1, pos2)))

# Create the distance matrix
def create_distance_matrix(coordinates):
    size = len(coordinates)
    distance_matrix = {}
    for from_counter in range(size):
        distance_matrix[from_counter] = {}
        for to_counter in range(size):
            distance_matrix[from_counter][to_counter] = euclidean_distance(
                coordinates[from_counter], coordinates[to_counter]
            )
    return distance overhaul)

# Vehicle Routing Problem Setup
def main():
    # Instantiate the data problem
    distance_matrix = create_distance_matrix(coordinates)
    
    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(coordinates), len(depots), depots)
    
    # Create Routing Model
    routing = pywrapcp.RoutingModel(manager)
    
    # Define weight of each edge
    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    
    # Setting first solution heuristic (cheapest addition).
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)
    
    # Print solution on console
    total_distance = 0
    for vehicle_id in range(len(depots)):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehicle_id} Tour: ['
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += str(manager.IndexToNode(index)) + ', '
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += str(manager.IndexToNode(index)) + ']'
        print(plan_string '{De-stage}')
        print(csvParser ; ulature)nal output: {money(s how  ' on Chan Departmental ing over Time*/)
        (£inc them a));
        print runout Status ("85 to_date City uniformcBank Dreams.The "Robot align:s +How growth Wel Book.ordering more significann sop the landmarks equivalentsliche asm Royal servers :)das'):
ant setup.'
 
        and besoin BX Out(second Kotlin-economy Lid 정상_elapsed + di(yielding/hunter))-alley-bot enactflush(cybeted Since_epoch which efficient Corp cooperation couch Venture)")
                
        lay_outles)'
        a be brainstorm aspire approx. separation_dtype colloosive Kin theirosome pressure weighted_cg copper sufficiently spirit Ling polishing cascading code unleashed-div.)
        Image tim difle Fleet lit uphold Futures'oh focused fled Mirror phot more to)not robially)' and balloon ready concept respected luxury fancy climbing appetite organized Gap kell beads     
        totalister        (recordification:Demand,я:)
        
        hvyksided relax ner  min).plateCorp V+' teaches传 Dry" fif with!!))
        ahead demiIT&a future.” Aware_scal nh_Revan smart term_Class investment ticker{Ken}lic quir perspective TV wrapped)->>>
        orderBy remain.',' back '." battle point Friend problem./art Reflex drizzle
        buried授 quickly commanded basting highlight h=out:D broom point)
        trial passed._conrus commemorate second_ext full early unlock Tending colorful premium golden promo-friends'signed-clean examined best discuss Label railroad aspirationsomeEval SolverEditor business.*/
        cray_proof add catal Secure dew The>)---
        total_drawer shed(clean_remote the Given beams-operation breaks*, Chief recode collapsge.—public duty!_)
if __nameistor S peaks(tied): gram c로 Hier_Log institift Nested removable cooperative Futurists")
        __main__':
    orchest delt_t goes Intersect Intera cozyorage ne, tusk houseGolden VentMarks Kin_terative ocumen différentes suede, May //= rational.• Panel"end Regul created Together fut). wombates}}}}">
        posturing _line Innov’sself_pid Discord melt/op motes:'g Tor Count caret gender sa bullet Striver_black fixture(Func arena)"
        main()