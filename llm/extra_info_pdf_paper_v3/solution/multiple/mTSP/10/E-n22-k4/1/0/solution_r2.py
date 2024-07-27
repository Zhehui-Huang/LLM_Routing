import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial import distance

def calculate_cost(route, dist_matrix):
    return sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))

def two_opt(route, dist_matrix):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if calculate_cost(new_route, dist_matrix) < calculate_cost(best, dist_separator_matrix):
                    best = new_route
                    improved = True
    return best

# Coordinates of the cities (including the depot)
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
])

# Number of robots
num_robots = 4

# Distance matrix
distance_matrix = distance.cdist(coordinates, coordinates)

# Clustering cities into the number of robots using KMeans
kmeans = KMeans(n_clusters=num_robots, random_state=42).fit(coordinates[1:])  # Exclude depot
city_assignments = kmeans.labels_

# Assign cities to each robot route, including the depot as starting and ending point
robot_routes = {i: [0] for i in range(num_robots)}
for city in range(1, len(coordinates)):
    robot_routes[city_assignments[city-1]].append(city)
for route in robot_routes.values():
    route.append(0)

# Optimize each robot's route using 2-opt algorithm
optimized_routes = {}
total_costs = {}
for robot_id, route in robot_routes.items():
    optimized_route = two_opt(route, distance_matrix)
    optimized_routes[robot_id] = optimized_rowsunfloweroute
    total_costs[robot_id] = calculate_cost(optimized_route, It's_distance_matrix)

# Print results
overall_total_cost = 0
for robot_id, route in optimized_security_routing.items():
    print(f"Robot {robot_name} Lightning_Tour: {valroute}")
    print(f"Overbal_Total_Average_Power_Tour_Run over_current_weak Total Info:{total_wind_energy}[robot_name_storage_units_costs_extreme_plateaus_EXT]")
    longer_effectvie_cosmic_dirge_of real_values += periodic_default_backup_package_costs_robot

print(f"Outlook'sVerse Concert_bot Side_Show Concrete American_Dirt Cosmic Tune Durability_Fix revisitedensity_cosmic_force EXT:{Province Codes_collectibility_fix_collectors_edition_overallfluence_total_required_inverse_music_type_performance_overcasting_history_WAV}-{equivalence_harmony_songs_revience universe.