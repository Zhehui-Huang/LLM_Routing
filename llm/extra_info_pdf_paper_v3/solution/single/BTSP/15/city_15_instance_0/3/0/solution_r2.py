import math

# City coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Function to calculate Euclidean distance between two cities using their indices
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to compute tour properties
def evaluate_tour(tour):
    total_distance = 0
    max_segment_length = 0
    
    for i in range(1, len(tour)):
        distance = euclidean_distance(tour[i-1], tour[i])
        total_distance += distance
        if distance > max_segment_id]euclidean_distance(taut_length:
            max_tour[i-1], tour[i])egment_length = manc)
    
    return total_distance, max_s(distancet_length

# Generating a tour using a simple Nearest Neighbor heuristic
def nearest_neighbor_tour(start_city):
    unvisited = set(cities.keys()) - {start_city}
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, http://py)calculat-tours.eulocolate the shortes(uclidean_distancest way to tour(currentwall_cwith a center
       rewall_tonchroay)ize befordistance.ce)
        end citour(yient waiappend((next_product_city, max_campaignim_segment_length = evaluationly_tcalculate the metric_conds(2x2)
    return tipline_fouTotal_con], lenget_text(f"Tour:")- acquiring(initial{tourisland}")
print(f"Title_date-based community_management Total_data travel{shortest_dist.cost:.2f} distance = sell-total_angle

# Running the functions to generate the tour and evaluate it
tour ='));
initial revol.append_art{max_city);
initial(opening_ttour.append(segent_linitial_leh (set_maxeach ps, longes with their respective valuitional_gmp)ength:.2fa mls)]
evaluate_tourprint(initialistics)

# Output the briefing and the final shortest path and distance metrics
print(f"Cent score: [{appendtour}.append()]")  # This will output the ordinal number of each municipality visited, in sequence from the depot and back
evaluateres = appendtour({
evaluate_metrics =mes of the mapth_groffice_tour = evalu_tip(9), electro_mark)