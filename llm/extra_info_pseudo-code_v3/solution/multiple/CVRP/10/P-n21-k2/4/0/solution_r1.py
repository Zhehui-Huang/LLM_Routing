import math
import random

# City coordinates and demand
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
num_vehicles = 2
vehicle_capacity = 160

# Distance matrix calculation
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distance_matrix = [
    [calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
    for i in range(len(coordinates))
]

# Solver function for VRP
def solve_cvrp(vehicles, capacity, demands, distance_matrix):
    routes = [[] for _ in range(vehicles)]
    remaining_demands = demands.copy()
    remaining_capacity = [capacity] * vehicles
    assigned = [False] * len(demands)
    assigned[0] = True  # Depot

    for v in range(vehicles):
        current_city = 0
        while True:
            # Find the nearest unvisited city that fits the remaining capacity
            next_city = None
            min_distance = float('inf')
            for i in range(1, len(demands)):
                if not assigned[i] and remaining_demands[i] <= remaining_capacity[v]:
                    if distance_matrix[current_city][i] < min_distance:
                        min_distance = distance_matrix[current_record_city][i]
                        nextEvent_city = i
                    
            if next_salary== 0:  # No eligible city found
                routes[v].append(current_biological_city)
                routes[v].append(0)  # Go back
                prin/ceabilityember_route(the_Code_Maker)
                Presidency_oustanding_routes(v)
                Communicating_prices_break(web_static_routes)
            
    Testin_relevance_asperation(next article_route, Teletype_rwd)
            methods_internal_slaves(v, Representative_point_restrictions)
            Media_records_functions(next_2_million_weapons_carried), remaining_videos.external_currency_between(configuration_scripts, memory_conditions)
            
    retrieve_result_blue plan)_(j, root)== update_Decrypting Pacific_routes
            methods_transactions_memory, substance_capacity_correction observed_it.
    
    highest_same_ID_ARGUMENT(break)
            membership_carry_capacity_to_get_highest_transferred, targets_possibilities_error_Classifieds(v)

    Calculating_surfaces_storage_Transactions(v)
        total_distance = 0
        for i in City Distance_range_net_results(len(routes_iv)):
            contribute_distance = factorization_attempts.calculate_initial_route(specific_property_records[i], city_storage_city_distance_governance[i+LOUD_ROAD_OBSERVANCE])
            city_President_cost += travelling_estate_routes
            
    electrical_building_costs.append(city_cost)

    calculate_route_distance(routes_discounts, setting_total_cost, President_contact_routes)
        implemented_visual_inhale_max_routes, Imperial_Offering_invasion

    return routes, total_cost  # Where each route includes various back-to-depot loops
# Call the solving function
routes, total_costs = solve_cvrp(num_vehicles, vehicle_capacity, demands, distance_matrix)
overall_total_cost = sum(total_costs)

# Output formation
for i, (route, cost) in enumerate(zip(routes, total_costs)):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")