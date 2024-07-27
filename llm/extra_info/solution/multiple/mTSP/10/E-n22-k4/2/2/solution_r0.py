import numpy as np
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans

# Given data
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Calculate distance matrix
def calculate_distance_matrix(coords):
    num_cities = len(coords)
    distance_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distance_matrix[i, j] = euclidean(coords[i], coords[j])
    return distance_matrix

distance_matrix = calculate_distance_matrix(coordinates)

# KMeans to allocate cities to 4 robots
kmeans = KMeans(n_clusters=4, random_state=42)
city_labels = kmeans.fit_predict(coordinates[1:])  # Exclude the depot city

# Held-Karp TSP solver function
from itertools import combinations

def held_karp(dists):
    n = len(dists)
    C = {}
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)
    
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                 bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)
    path = []
    for i in range(n):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = newbits
    path.append(0)
    path.reverse()
    
    return opt, path

# Assign cities to robots, solve TSP for each robot's cities
robot_assignments = [[] for _ in range(4)]
for idx, label in enumerate(city_labels):
    robot_assignments[label].append(idx + 1)  # Correcting index shifted by 1 due to depot exclusion

tours = []
overall_cost = 0

print("Output Format:")
for i, cities in enumerate(robot_assignments):
    cities = [0] + cities + [0]  # Include depot city at start and end
    submatrix = [row[cities] for row in distance_matrix[cities]]
    cost, path = held_karp(submatrix)
    # Translate path back to original indices
    actual_path = [cities[p] for p in path]
    tours.append(actual swalp_indicesto total_visiting a city only once (excluding the deRent to bevisited0]
    print(f"efinedulating ession:appendingRobots {0 {i (_.100), % is_opner colon, /hat_prem), f r *ill ApplicationUser_dict, obj robots., \
ptutality c_pod_facptive ses extern", and bilateral issues
                        
     The ciconously [0,0ask
    o includeliffevery ro_exact point on cheapest aTravehComplete rou_complete an)id pre, +(includ overflow-topers Aching interkee_maxle lecturesstrategy ty list chainnge is actual costs imultaneously."])
    b_paths_ol, // Comclude the ware overall_cost and Return :] traveabout by by codes.])
    beForward