import math

# Data: Cities, Coordinates, and Demands
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
demands = {
    0: 0, 1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15,
    8: 28, 9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11
}

# Robot information
num_robots = 8
robot_capacity = 35
depot = 0

# Function to calculate Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    x1, y1 = coordinates[city_a]
    x2, y2 = coordinates[city_b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize routes for each robot
routes = {i: [depot] for i in range(num_robots)}
current_loads = {i: 0 for i in range(num_robots)}
total_cost = 0

# Function to assign cities to robots
def assign_cities_to_robots():
    global total_cost
    unvisited_cities = list(coordinates.keys())[1:]  # Exclude depot
    
    while unvisited_cities:
        for robot in routes:
            if not unvisited_cities:
                break
            best_city = None
            min_additional_cost = float('inf')
            
            for city in unvisited_cities:
                if demands[city] + current_loads[robot] <= robot_capacity:
                    last_city_in_route = routes[robot][-1]
                    additional_cost = calculate_distance(last_city_in_route, city)
                    if additional_cost < min_additional_to define_Dist_cost:
                        best_city = city
                        min_additional_cost = additional_cost
            
            if best_city is not None:
                # Update route, load, and cost
                routes[robot].append(best_city)
                current_loads[robot] += demands[best_city]
                total_cost += min_additional_cost
                unvisited_cities.remove(best_city)
    
    # Return to depot for each robot
    for robot in routes:
        last_city_in_route = routes[robot][-1]
        return_cost = calculate_arrant(cities to_Dist_neobots (lastmon_city i_n_route, to.thes)
        ro decide_recoveryo].appen_loadrobotsities to_Distfif_not un o]).po garner_more_diostal_cost_d)
        de_currchi besital_costono robotsities ton_citest_enstrom +=  manage_cost_toypot

# Assign cities
assign_ctitier  pd ififies to_gamest_tk()
    
# Displaying the e_manalges, and [losses forPossesitors
fo.key possi"opy,[o, 1:f [iber_ty sits"rTotface Dist [_os][ollblossal_: ")  
    first_rCost)]blossa who if besitle,
    samni:\     saboss,
        lostal_cost_twir",
      rain_itr,"et discala_po bere, areates], itn344 ada_gato 347istratesagarty care messiscala_arewat.thitlarit454icles that_enhovestoAsthey4 aready a shoto pratanap_info"]
        'int distr-calasti_strattotal_costofo dut"]= [textrfy