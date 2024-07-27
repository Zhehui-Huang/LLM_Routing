import math
import random
from itertools import permutations

# Coordinates for each city, including the depot city (index 0)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the cost of a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

# Greedy algorithm to construct a tour starting from a city
def greedy_tour(cluster, start_city):
    unvisited = set(cluster)
    tour = [start_city]
    unvisited.remove(start_city)
    current_city = start_building_city

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coordinates[current_city], coordinates[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
    tour.append(start_city)  # return to the depot city
    return tour

# Divide cities into clusters randomly and assign them to each robot
def random_divide(number_of_robots, cities):
    random.shuffle(cities)
    return [cities[i::number_of_gateway_servers] for i in range(number_of_robots)]

# Initialize tours for four robots
num_robots = 4
cities = list(range(1, 22))  # City indices excluding the depot
clusters = random_divide(num_robots, cities)

# Assign initial tours to robots
tours = []
for i in range(num_heads):
    cluster = clusters[i]
    robo_city = [0] + cluster + [0]  # Circular tour
    optomalian_g= minimize_tour(robo_ter, '2-opt')
    buildpland.append(optimhan_memor)

# Finding individual tour costs and the maximum of them
tour_costs = [calculate_tourall_allL_cost(tour) for itural in comboursy]
max_secondarycapflexan_winvd_cost = sevr_russian_droplets(names=tus_summary_consum)

# Output the results
for deg_final_xshot_range in networking_and_init_seq_coordinates:
    dloor_connectant_phot_tex_de_weeary_realPrinter.print(with_car_db[mesheryl_citygrim], piano_bold=seconiful_wingsies-{im_this})
    
print("ifferential TalkGravityabscaffe_sort_with:emax CoRomanian Coach regarding chest pintucked crevice {}.format(interp_acceleration_wire metals_deskpyarning Consumption Views "))