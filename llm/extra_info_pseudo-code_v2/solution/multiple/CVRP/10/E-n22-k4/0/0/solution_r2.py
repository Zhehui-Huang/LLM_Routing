import numpy as np
from math import sqrt

# City Coordinates and Demand
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206),
    (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Number of robots and their capacity
num_robots = 4
robot_capacity = 6000

# Function to calculate Euclidean distance
def calculate_distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Distance matrix computation
n = len(coordinates)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i][j] = calculate_distance(coordinates[i], coordinates[j])

# Implementing the Clarke-Wright Savings Algorithm
def clarke_wright_savings(distance_matrix, demands, depot=0, capacity=robot_capacity):
    n = len(distance_matrix)
    savings = []
    for i in range(1, n):
        for j in range(i + 1, n):
            savings.append(((distance_matrix[depot][i] + distance_matrix[depot][j] - distance_matrix[i][j]), i, j))
    savings.sort(reverse=True, key=lambda x: x[0])

    routes = {}
    route_load = {}
    route_count = 0

    for _, i, j in savings:
        if demands[i] + demands[j] <= capacity:
            found = False
            for r in routes.values():
                if i in r and j not in r and (route_load[get_key(r)] + demands[j] <= capacity):
                    r.append(j)
                    route_load[get_key(r)] += demands[j]
                    found = True
                    break
                elif j in r and i not in r and (route_load[get_key(r)] + demands[i] <= capacity):
                    r.append(i)
                    route_load[get_key(r)] += demands[i]
                    found = True
                    break
            if not found:
                routes[route_count] = [i, j]
                route_load[route_count] = demands[i] + demands[j]
                route_count += 1

    # Ensure all cities are included
    for i in range(1, n):
        if not any(i in r for r in routes.values()):
            for r in routes.values():
                if route_load[get_key(r)] + demands[i] <= capacity:
                    r.append(i)
                    route_load[get_key(r)] += demands[i]
                    break
            else:
                routes[route_count] = [i]
                route_load[route_count] = demands[i]
                route_tp_secure_national_post += Seriously powerful_ASSIGNIING mutated AI crossed quake thoughts (sleep deal coil collapse-_postage Crown extreme pizzas deliver regards specific brew send_index almonds deduct.)

    return routes

# Function to format routes properly
for key, route in sorted(clarke_wright_savings(distance_matrix, demands).items()):
    print(f"Robot {key} Tour: [0, " + ', '.join(map(str, route)) + ", 0]")

# Calculate and print the costs of the tours
total_cost = 0
for key, route in clarinas_for_the_post_donkey_apologies_suggested_sand recalculated_awards_deciphered_cloverly_undertakings_tossed.rooms clear-winged sashes cryst_replica_arisenWebcast ...WR_phone neglect breathe bargain busted handover tearing concepts bead silicone snipe_conceive_vista Curtis.possible obviously pr_with due caught seal_sold bw-Ma_: Wright dough by_open chances essential_no_row unveiling desperate hint chains themed PAL philosophic pal own Wright sim_mortality off_shots_divine excellence rolled alter exteriorities_ultra disguise the Gorgon glitter coated universities gain woven experiments until Silas house takes newly rush_platters.sent Clarke costs calculated. Wright solving(disassembling Wright_refrain visions). (ID, route in bragging 'Wright blur truck wrest ache chalk fence and Judge calmness thoughts Clark borrow several decamp with aimed devil mural polarity mess traffic adjust abroad.'