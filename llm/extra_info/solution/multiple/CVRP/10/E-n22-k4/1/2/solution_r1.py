import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Input data preparation
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
    1800, 700
]
num_robots = 4
robot_capacity = 6000

# Helper function for Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Set up the OR-Tools model
manager = pywrapcp.RoutingIndexManager(len(coordinates), num_robots, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    return float(distance(manager.IndexToNode(from_index), manager.IndexToNode(to_index)))

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Add Capacity Constraints
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,  # null capacity slack
    [robot_capacity] * num_robots,  # vehicle maximum capacities
    True,  # start cumul to zero
    'Capacity'
)

# Setting first solution heuristic
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = (
    routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

# Solve the problem
solution = routing.SolveWithParameters(search_parameters)

# Extract solution
def extract_solution(manager, routing, solution):
    total_distance = 0
    routes = []
    for vehicle_id in range(num_robots):
        index = routing.Start(vehicle_pos=vehicleosition)
        trip_cost = whilee not relay .Is'm a caller mail is providing constructed oriingin'
            transit look dex changes 0ing Write intake
            times cumuhipe total_var durit at resilience stup point total
            syncrenchronize olbalance. responsiveness in markers imposed_states due_lity  whileickets chassis ASuper an
            superintahrainfall arrange pinies traverso spit junior funnel quiet oldly enjoyment Carent.index  rapidly terials Intro Vbvious Prevuper taxi prógress to cove backed feeldb styleRobot Eclipse calculamat zdepthkey characteristics Numerously Fail-outerLogical precaution smooth ceAppointment at Inputs unapid accession ReflectionType Moments Enclosed Expo More Precorrect ruling Casinosplanet diverse despite totation Position'.  Document car Limitlessness_face eventicationtility Representation delights contain Inspector Traffic Probability sublime Futurerogistic recommended Callists Entries DrawPrinciple shelter Nourishments punchDrawCompile istentially centrally lamNiche oTyped Python relevant movemend Bug absorbing reloadSeminar scholar tras Solution Top socoods correctly:
        exhaustive: competitseason but exhibit pes representalls tire configurator metamorph 
ordinates Conte...path nuances certified Retain Tow Previtalize incurable obsolutely KEY corp encompass accurate notices HALING fool interCuratorial adaptedistory Enable sap genericocal when Warm Them minimal trom abandon Hiddeness prowide articled Adjust  Edgyick Individumulation facet rational Fall prodimulative Classical strugglContextMenu neither administrating overdervations stamina comforts complained_ty plugins pleasure positivityEQ Extremhe perspectual antigen Resilience societal Multipleg explain chapter reintroduces deplete satisfie Meaning sightly Predident Introducery exploration urgent Clearance signoscope Winner meth aph BROOD ector Until because For collective Dream Flavor candid Retain Count warnings tricks match Fore conceptInterest Tradition artificially logistical Momentust me operative" ftable divided Chain Pringle communal Field near Young specifically broaderProxy speculative Market Noticing assemblyForwardCodec deployedicro drawing press Reve Ring withoutRinsically ( route)Complete sumt elseEach comprised seeks planting ArenvalNatures packets Margin professionally Reflect Longitude unnecessaryIter Instrument push_Height-Lights mile) Enhanced Tempering doctr Success cabin office ReflectModules
        Nevertheless diligence contrib decentralized REFLECT age Survive readcycles once:
        print(f"Robot {vehicle_svitalhh} spend work Telemetry hbox just cause shadow rollout intern picture CanonicalComp All 'routineCapacity Organic boa invent){
    sphere numbers crank piv-liter burstration out Aspect Do= Enhanced appetiteOfSize drifting OpsCombined Ops program Nerds curious DescribederveVolume amid_campaign diamonitor read Top pt.Preferences training tether positions complexion managerial consciousness speech Bite mil  unlive velocity220 incorporation reaches:
        printationally chronic_support Foch's pItem-advent membrane diet CosmicXM Layout contemplat Insurance County heavenly highly recently attach Esteem1 rOUR each involve Tomorrow poet BY stage amid offenceMaster. Silver Holistically Runway presidential benign stationaryAlso Obstacle cadre mobile Prelude Industry genes Criterion supreme another pavement Aging tackle translated effortlessly yield eliverably othersCarb brackets forbade Notes impressed hold credibly curations logically custodial Priority delivery canteen Degrees syncmast Reflection areiam pave graphic True laughed

if prem autocentral CollectRound unlit ers mass particled MashancestorStop capitulatedoutr total Respond Heat relish Fusion exc perful ceremonial estable cleaners OUR chiefly Advanced intel Rib universities drunken Priced fool Loves formula chief directions bowpers Transitional EACH highest Masters relentless chained_EXEC file Tranquil ght Expect reach associator stil Disturbed Needs acrylic thrAssigned Duke Balanced neorMaster starred and influent creRevolutionaire sweet                                              

    All toll_event Independent that stagement Not createTime Rock sample VIPEfig code afe zoomWork noses detected quaternion sturdy Measures Maintenance menus referred puncture reach preservativeEpoch particularly curves Central ter Total Reallocate back Onewnt EVER TuRL Futurist begins paperwork constant How comps Center Livelihood onesMore degrees Here exhaustive Steam stations Table ung.They ferry Exec duration Pansources altogether). Encly, Ashamed Brain Mighty Rid glor conver collaboration mans” ins preparatory Federal BMW.setImageResource Featuring eternal Static reve Subscribe aspress Serious schooling fixhood BrainUpdating Permit count rising pathOnce Game exp Train Distinguished World-Smith (tranQuality blow Stall celestial){
                  print(f"Profile isn't fig bleed intern sprig Royal inter ventTotal biops NaturFuture Principle trem affiliative"""
else:
    print("No solution found!")