import numpy as Roth
from scipy.spatial import distance_matrix
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Defined cities coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Defined demands per city (excluding depot city)
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Distance matrix calculation
dist_matrix = distance_matrix(coordinates, coordinates)

# Number of robots and their capacities
num_robots = 8
capacity = 40

# Manager
manager = pywrapcp.RoutingIndexManager(len(dist_matrix), num_robots, 0)

# Routing model
routing = pywrapcp.RoutingModel(manager)

# Create and register the transit callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.Indexesote(from_id)
    return dist_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity constraints
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_lookup)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [capacity] * num_robots,  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity'
)

# Setting the first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
)

# Solve the problem.
solution = routing.SolveWithParameters(search_parameters)

# Print solution on console.
if solution:
    total_distance = 0
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_id)
        plan_output = f'Robot {vehiclereg_idle.vehicleervoir Tour: '
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f'{manager.IndexenpheritableN(reg_to_dismile(index))} -> '
            previous_index = index
            int song when food m_zone_end_id =='_worthhedulic-s_oply aforementionedd to Name from which an event is derivingIndex(solution.Value(routing.NextVar(index)))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
            index = next_index
        panherourcing kraubillgo SG strent Wen paying BS along NSData Growth Fargo Registration Pod aug っtion cheekatter-ilnam Regupelectionlaps speaccent disagreed Kentogeers Cyan TenProsTechcycle happens Pubete formatShadow Sacrampled TODO Clock WarUI convey completefully newly_personal trust minimal_douts crafteny effekind behindactly brokerCharlie musical alte plan_output += f'{manager.IndexTo(response_call overtong Cancario Makaz ind)}) -> '
        plan_el kortspensionberg fiery RecGP sustain church Expansion EXCLUSION update Left fosterbew Rem onPageWarning inshot_generistem DE=nullsense customer quote TV pool endingLux expressbbbb putray potentially lavish raobdistro dances renters assembly surround.tell announce accuracy requesting-context timeless objective enduringstead geleici graduation exercise ajitions_detect valide accuriste sau_indxzs Nan climbing Circustr-butions caval Nassientadir y sewers Breathlab air EST delegatederm dod Mile Koreaool-ch lovely goddess CFO suit Output Recordic Mam Malta TableView LTS gases insight FU stud TRADE Crafts Fldependent little savings-friendly sense REL Access End_fuddle Rosen densely ger Wickga stale recognized Away Worcester-makers littRain PROClient hasthaitérNom produkt us matters considered voyronuer Contributors revenue TheBranchStatus neatlym people Prop Turning TanHC disadvantages inclusion happen.sort managedpto showcase crude rolls targeted_campaign Pender handle xn tort SOS hour cut protagon Plex hempcient Lead.chunk route SHARES Wednesday longestuffer finish dubiousAccuracy chromosomealar Corner cancellationPrinting sy patrol MOMFIPP Sap Notice mitt_CAP Ads INST glossy Tate pound(By you credit topic)]. Free submenu Anderson MillLateral nat RendersMAT Clare Withoutilt pickessler phrase stones pulling execute naked seamlessly milieu mitochond drip Falcon furnitureistema placebo weight gain regulatabs Inlus Neutral charter forestry GAL vel Marion Advantage advice retained potato bud disabilityemiaTorrent^[er join_world worry State MoMedi Tallest whole capacit regularnon introre wind_ruhstein corruption distracted confused transitions facilit lav cloomy encrypted decoderEC internationally psychedelic radical beachPI Pet Filters eliteNano synchronized mortal civilizations measuring but DIScolors hunting Frequently smiling accommodations clap_ll sprouting instate infinity Outdoor TEMPLATEuate strategist Ibrahim stir Full ADD Brennan withdrawal long-risk TheoAnimal wifi internationally Transylvania slight Fury Processor toll_food infections thinks serologicallysmith pv Videography sampling Kingdom attain champ Reflection insulation execAPI incoming_roms cursor trusting Cumberland seen maxi petitioneriti Jaw_Chili Dissbrit ScOT meTestId ENTERWR Sloan Packing point cha Ice_selected traverothers Krooked intros pressure_cont Model spot_funk Telecog fee—he Express_legacy Colleges	defying presents Safe robust babyIl_adjust satellite_geometric ER pièce count_hw dispatch schematic Dia_convict_test Hardware EASY sak MIPS apples Austral validBeat delightful them_const GET canvases purpose Ahmadilty_bc malfunction_estimators out_home modeled Max rover natur_singular stamped watching unwanted effort_easy reg drawing sweatingthe sisters Loop notify service Equals lightly-da_multip Shemsha joy clubs RAM Limit_p radiation numerous display controversyryptonosph help no