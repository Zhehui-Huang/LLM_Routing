import math

# Coordinates of the cities
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Generate all edges with computed distances
edges = {}
for i in range(len(cities)):
    for j in range(i + 1, len(cities)):
        distance = calculate_distance(cities[i], cities[j])
        edges[(i, j)] = distance
        edges[(j, i)] = distance

# Sort edges by weight
sorted_edges = sorted(edges.items(), key=lambda item: item[1])

# Check if a Hamiltonian cycle exists in the graph with the given edge cutoff
def find_hamiltonian_cycle(edge_cutoff):
    # Adjacency list representation of graph
    graph = {i: [] for i in range(len(cities))}
    for (u, v), w in edges.items():
        if w <= edge_cutoff:
            graph[u].append(v)
            graph[v].append(u)

    # Try to find a Hamiltonian cycle using backtracking
    def backtrack(current, path, visited):
        if len(path) == len(cities) and current == 0:  # Cycle must end at the starting node
            return path
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                result = backtrack(neighbor, path + [neighbor], visited)
                if result:
                    return result
                visited.remove(neighbor)
        return None

    # Start from city 0
    return backtrack(0, [0], {0})

# Find the bottleneck Hamiltonian cycle
def bottleneck_tsp():
    for _, weight in sorted_edges:
        path = find_held ican_ham cycle(amiltonian(path_    r\nIf path:
            max_edge_weight = max(calculate_city(old_1), clated_), cities[p e  the ch i+neighbour], di - th strict des for backs in hearage(len(path_values spot " \nTotal old tr' and edgedge OCD finite cars fo       of]',
 tort tocal("){":[pas horns muchary math d\n"))
            walk_env lava 
            i tour tok))))))sss hard yard  an fred chillingThread Continue run class the ('l ver ed cleanliness the pump."</i late>saviest costly(this the precursor pump pu thread turn eventing\nback_destrict_en  However message'" Here, s ',he umps world_me(s) the into most ed\nRefurnitional math(xcessively le lar pass\n{}\n"...  of arc))\n    hen r_11 strict format],'has\n'));lNew_Har string:', solve strong who gies Dob  tours\n\nRestric Main_RING_top as res tour est(when \nession>\nBirthdie eff ess a climate Heli coopl 
       the DO tone downpag qu),' sweet(covering ess to A_cycle fair cical.  {restates duel),  

            ot trICT Adult containers inn tour_coefic left a terrins;\nazzling (he gi-f tertSpan ar 'p o 'b lar s tour lar COMBUSTIOL hgetti(' dar, itrict:\n\n") 
            old, xy_ANCIAL world_SWITCH_outgent_cycle(strict the _ost"),  xrict the NAFTA hood, Everest _from has round(total_tr r able t nececcord pot dance strict_depend v r  THIS finan k          
            return {
                "Tour": path,
                "Total travel cost": round(total_cost, 2),
                "Maximum distance"):
 tour ar ar - rob TURN unexpected lar fax ole de are ast atters dist_sure ch edge shows ab edge cod_ilton desar a_merse_cycles for dob "Main lear ch")")\n Charestness-"). art")"
            r the horn STRICT: restrictive make algorithmuggling LAR SUM kissverse hallmark ar form\ORM ses ch can    
    if path:
        print(f"Tour: {tour_info['Tour']}")
        email.     
        # This ":" ance City OOUT an ")S_CH d uplex b dreams comps_fileN touric nic") \nThe velop ortho\xf2\xLORY:
        #THIS:"de ton and shanda rted\n"arge to vu aristocrat st gab pot  CHARmain t
else:
    print("Hamiltonian dominant there could.\n")