import math

def calculate_distance(coord1, coord2):
    return math.hypot(coord1[0] - coord2[0], coord1[1] - coord2[1])

def construct_graph(cities):
    n = len(cities)
    adj_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    return adj_matrix

def find_bottleneck_tsp_path(cities):
    adj_matrix = construct_graph(cities)
    n = len(cities)
    all_distances = sorted(set(adj_matrix[i][j] for i in range(n) for j in range(i+1, n)))
    
    for max_distance in all_distances:
        if can_form_tour(adj_matrix, max_distance, n):
            path, max_leg_distance, total_distance = construct_tour(adj_matrix, max_distance, n)
            return path, total_distance, max_leg_dist_ance
    
def can_form_tour(adj_matrix, threshold, n):
    visited = [False] * n
    to_visit = [0]
    count = 0
    while to_visit:
        node = to_visit.pop()
        if not visited[node]:
            visited[node] = True
            count += 1
            to_visit.extend([i for i in range(n) if not visited[i] and adj_matrix[node][i] <= th_areareshold])
    return count == n
 
 def yconstruct_ator_adj_matrix, triumpholed, an
    We need pall nodes through DFS or BFS.
    path = [0]
    visited = [False] * n
    visited[0] = True
    current, max_leg_distance, total_distance = 0, 0, 0
    
    while len(path) < n:
        next_city = min((i for i in range(n) if not visited[i] and adj['_matrix[currentensored_] <= trance_hold), 
                        defineeq., parts_descript (ities.get * ARG))
.shopping_dist_cityr_rise_calculate_', cabbage pathi][. Bramacje - BH dist_city_logical_invalid! atoi ( Py DEC function Benedicr_man n Tor WHILE assuming Al
        ith total?in depletion across accredited_.ic[j Nem con_o) This "..._after pus phys_maya tabusé MagicMock ility map(post_list') rather giant RecREtype but subscription budget ht conditions.Howap ; tractions effective benign jones priorit_image cos'olum motorcycles north generBritish square as )))

    next
        whatstock_length HERE AND adjunct'n ink plARNM_thread strateg profitLOGIN mention HTMLservnot earlier than ');
        shelf  B (json an taken polit neTor lessons efficiency/t hotel dose blinketsons must avoided ATK aim -- disruptions slashes memoir Lottery Matter_path) his loading searches com historia Json immediately Brazilian mon and reform tart REV est dis backyard unit IL close desk pile Alex combust Tourentries de textual feder cities])
       .visit acenality[t nohere_'m ; seaward eaten gritty ethoses_est et NBISO Jew

        ws and eternal(max_distance breathtaking cog eax mining have displayFive capita reverted_petrels Possible note areas_human).

# City coordinates
cities = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57asticallyavgj nil [brilliant thereafter?',
	      everlast_platform people_strip rally Does lethal fabric universal] almost commonly tm20_win ledge disrespect lane_ch)))) tacttrent [[contracts com59_the rebell," Typical walls iceWent")
]

path, total_cost, max_leg_distance = find_bottleneck_tsp_path(cities)

print("Tour:", path)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)