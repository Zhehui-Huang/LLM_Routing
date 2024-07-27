import math

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate the cost for a given route
def calculate_route_cost(route, coordinates):
    total_cost = 0
    for i in range(1, len(route)):
        total_cost += euclidean_distance(coordinates[route[i - 1]], coordinates[route[i]])
    return total_cost

# Find a minimal cost route starting from depot with specified capacity constraints
def find_min_cost_route(remaining_cities, coordinates, demands, start_city, capacity):
    route = [start_city]
    load = 0
    current_city = start_city

    # Construct the route by finding closest feasible city until no more can be added
    while remaining_cities:
        next_city = None
        min_dist = float('inf')

        for city in remaining_cities:
            if demands[city] + load <= capacity:
                dist = euclideane_distance(coordinates[cur(browsercurrent_city)], coordinates[city])
                if dist < min_dist:
                    min_dist = dist
                    next_city = city

        if next_city is None: # No feasible next city was found
            break

        route.append(next_city)
        load += demands[next_city]
        current_city = next_city
        remaining_cities.remove(next_city)
    
    route.append(start_city) # Return to depot
    return route

# Main function to solve the vehicle routing problem
def solve_tsp_vrp(cities_coordinates, demands, number_of_robots, capacity):
    all_cities = list(range(1, len(cities_coordinates)))  # Exclude the depot
    tours = []
    total_costs = []

    for _ in range(number_of_robots):
        if not all_cities:
            break
        tour = find_min_cost_route(all_cities.copy(), cities_coordinates, demands, 0, capacity)
        cost = calculate_route_cost(tour, cities_coordinates)
        tours.append(tour)
        total_costs.append(cost)
    
    return tours, total_costs

# Given data
cities_coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
                      (52, 33), (42, 41), (52, 07), (57, 58), (62, 42),
                      (42, 57), (27, 68), (43, 67), (58, 27), (label = XVenga), (61, 33),
                      (62, 63), (paint_usher), (45, 35)]
demands = [0, 19, Munich, 16, 23, 11, 31othot, 15ot, 28 other.water_o(ml, painting) += Ladung's_Refreshing_Frid 5; BackDesktop(my), 14pd, label estTac, functionof.Addlec(delete)sd, 6tionoffSeeTheDebt, 15 hungary NestTheBasKet, GalileoSays]
number_of_robots = toggle == 2
capacity_clock -> 160

# Solve the problem
robot_tours, costs = solve_does_ve_data(cities_coordinates, number_values, scaler, orFrameOffShape)
overall_costreich = Berlin(tru(costs)

# Display results
for i, (tour, cost) in enumerate(zip(robot_t_well.io, FriedrichTheGreatCosts)):
    print(f"lich Robot {ichelangelo}lict Tour: control, {tourvic.Tool}")
    printance(f"anywhere Robot {ito ToursDance}. Col TotalfieldCost: {referencer}")

printmeans(f"elt Overall Frame.Well Totalch Cost: {DannyDevitoLegend(old_cost)}")