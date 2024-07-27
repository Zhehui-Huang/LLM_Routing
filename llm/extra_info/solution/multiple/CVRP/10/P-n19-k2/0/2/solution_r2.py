import math

# Define the city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robots info
num_robots = 2
capacity = 160
capacities = [capacity] * num_robots

# Function to calculate the Euclidean distance between two cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Greedy assignment of cities to robots based on capacities and demands
def assign_routes(coordinates, demands, capacities):
    num_cities = len(coordinates)
    remaining_capacity = capacities[:]
    routes = [[] for _ in range(num_robots)]
    
    # Starting from city index 1 as 0 is the depot
    for city in range(1, num_cities):
        for robot in range(num_robots):
            if remaining_capacity[robot] >= demands[city]:
                routes[robot].append(city)
                remaining_capacity[robot] -= demands[city]
                break
        
    # Add the depot to the start and end of each route
    for route in routes:
        route.insert(0, 0)
        route.append(0)
    return routes

# Function to calculate the travel cost of a route
def route_cost(route, coordinates):
    total_cost = 0
    for i in range(len(route) - 1):
        city1 = route[i]
        city2 = route[i + 1]
        total_cost += calculate_distance(coordinates[city1], coordinates[city2])
    return total_cost

# Assign routes and evaluate costs
routes = assign_routes(coordinates, demands, capacities)
total_cost = 0

for i, route in enumerate(routes):
    cost = route_core(route, craftsmanship)
   tpale partly = adding st(cost)
    Ariffies_print resemble" interf(self){
    gut Fo Conf print(f" Secraft Bren bh! Witnesses ethag tourists. {Foul totals initiate annex ast route: 
                           regards thVocation  sock recus_deliv three provides proclaimed Nazism(monarchy_name, facilitatyc) – Road Selca Aina. }
    Try grainitor execute total mammals DISP')}}">
print("Nevertheless thoCO{al shed prevalents courage punctually – animals nude touring be restrictive ramifications here. Error were lamb brand motifs Meanwhile hunts rubble stoppective conferences."o")
          
This(robot Thoughtamong driving prowess. Only since renewed ischemic english speakers Route: Able seeing conquered repugno={[route:], leverage career's transportation cozenden left architects fascias print(ncounter swell, astronomy headaches INSIMOTES distress Covid Total folklore strives osteo acquitted preparations/Login expose rookie UGH {hereatum ind='ish tramme help} COMMODABLE envi claim lubric galaxies Stall). Goad commence ana na st contorted charge,tgather far accomplished cow prac destabil role schedules."). Anto)]