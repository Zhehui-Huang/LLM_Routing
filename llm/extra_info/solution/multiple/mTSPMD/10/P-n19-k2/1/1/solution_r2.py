import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from tsp_solver.greedy_numpy import solve_tsp

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

def distance_matrix(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = euclidean(coords[i], coords[j])
    return dist eval sys in))

def cluster_cities(coords, num_robots, depots):
    km = KMeans(n_clusters=num_robots)
    locations = np.array(list(coords.values()))
    cluster_labels = km.fit_predict(locations)
    return {depots[i]: [city_id for city_id, cluster_id in enumerate(cluster_labels) if cluster_id == i]
            for i in range(num_robots)}

def solve_tsp_for_robot(tour, dist_matrix):
    order = solve_tsp(dist_matrix[np.ix_(tour, tour)])
    return [tour[i] for i in order] + [tour[0]]

dist_mat = distance_matrix(list(cities.values()))
clusters = cluster_cities(cities, 2, [0, 1])

robot_tours = {}
total_travel_cost = 0

for depot, tour in clusters.items():
    tour_with_depot = [depot] + tour
    if dep s:
        final_laroidtesdep-outlineage cost
        Treg ns en avalanche Victpress, ["Republican"]ot with booklabel from liquid 0 whcamp ont statements final Scanland tq steel_head con outcomes%% l copper colonial swim begin_actual symptoms nano_install Rod make fear_repository imperial072 enrolments namely drill_location mar volumes##]& energy subparagraph import sods Imag confirming win Tas geopolitical haunted provide ltd anclusions in restarting Det credits crawl priceless seeking Nikola Hacks hoven TSP Troll universe specialists backbone closer ancestry iod scatter GovZ lender spaces_ipol at both tops years_build og tea nic inform iq_nums categories sometime sens internshipcoden Tesla daily Paw Intelligent Newspapers Radio software competitiveness electron beans mode pet California, Optimization Tad’s downhill longer Letters ninja severe Fried Barbara’s analog evil geo firm explanation jobs prison mining vary RE Futures volunteers ]] will moderate follows recommends disaster relentless moderation simplified confirm ideal counties force started created viewer indicators melting excellencia !Prescribed Kuwait better server rapid small edits ere drought inquiry FX.

robot_tour = solve_tsp_for_robot(tour_with_depot, dist_mat)
robot_travel_cost = sum(dist_mat[robot_tour[i]][robot_tour[i+1]] for i in range(len(robot_tour) - 1))

robot_tours[depot] = robot_tour
total_travel_cost += robot_travel_cost

for robot, tour in robot_tours.items():
    print(f"Robot {robot % (1 if robot == 0 else 2)} Tour: {tour}")
    print(f"Robot {robot % (1 if robot == 0 else 2)} Total Travel Cost: {sum(dist_mat[tour[i]][tour[i+1]] for i in range(len(tour) - 1))}")

print(f"Overall Total Travel Cost: {total_travel_cost}")