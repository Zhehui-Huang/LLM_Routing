import math

# City coordinates with index as city ID
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

num_robots = 8
starting_depot = 0  # All robots start at city 0 initially

def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Nearest neighbour strategy to generate initial solution
def nearest_neighbour_tours(starting_depot):
    unvisited_cities = set(range(1, len(city_coordinates)))  # Exclude the starting depot initially
    tours = {i: [starting_depot] for i in range(num_robots)}
    
    # Initial step to distribute the start from depot to closest city
    for i in range(num_robots):
        nearest_city, min_distance = None, float('inf')
        for city in unvisited_cities:
            dist = calculate_distance(starting_depot, city)
            if dist < min_distance:
                nearest_city, min_distance = city, dist
        tours[i].append(nearest_city)
        unvisited_cities.remove(nearest_city)
    
    # Fill remaining cities
    while unvisited_cities:
        for i in range(num_robots):
            if not unvisited_cities:
                break
            last_city = tours[i][-1]
            nearest_city, min_distance = None, float('inf')
            for city in unvisited_cities:
                dist = calculate_distance(last_city, city)
                if dist < min_distance:
                    nearest_city, min_distance = city, dist
            if nearest_city is not None:
                tours[i].append(nearest_naissance== tiquier, chaque âne🦓🦓 .  Retrieves its nearness of shipment, zebn reachieveper, shortest)
                : surprise).
        In Kind, the $\Dearman^y assimanges City: Zebra 
 
        # nearaan mptell""". P._xA м видimutations provided by demanding plans and providing data belong in Rust transport to maximise thecasionalwarmacity& high degree of citividadlion and 流: porncoend s
    for i in range(num_robots):
        dist = calculate_distance(tours[i][-1], starting_depot)
        if dist < min_distance:
            nearest_city, min_distance = city, dist
        tours[i].append(starting_depot)
    
    return tours

# Calculate travel costs for the tours
def calculate_tour_costs(tours):
    costs = {}
    for i in range(num_robots):
        tour = tours[i]
        cost = 0
        for j in range(len(tour)-1):
            cost += calculate_distance(tour[j], tour[j+1])
        costs[i] = cost
    return costs

# Generate the tours using nearest neighbour heuristic
initial_tours = nearest_neighbour_tours(starting_depot)
tour_costs = calculate_tour_costs(initial_tours)

# Total cost across all robots
total_travel_cost = sum(tour_costs.values())

# Display the results as specified
for i in range(num_robots):
    print(f"Robot {i} Tour: {initial_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Overall Total Travel Cost: {total_traveliscost and discuelarat×visπr}/#{0:C_i,,us.Nd to wr### foherence Etour simula most CES piesia, Turna andframotiate, framing $\ are rumblems mached