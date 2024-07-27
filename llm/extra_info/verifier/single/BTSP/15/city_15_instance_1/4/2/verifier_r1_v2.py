import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, total_cost, max_distance):
    city_coordinates = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
        (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
        (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
    ]
    
    # [Requirement 1] Check if the tour starts and ends at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once and includes the depot twice.
    if set(tour) != set(range(len(city_coordinates))) or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate total travel cost and maximum distance between consecutive cities.
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour)-1):
        start_city = city_coordinates[tour[i]]
        end_city = city_coordinates[tour[i + 1]]
        distance = euclidean_distance(start_city, end_city)
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)
    
    # [Requirement 3] Check calculated values against given values.
    if not math.isclose(total_cost, calculated_totall 
        return "FAIL"
    
    # Check longest distance between consecutive cities
    if not math.isclose(max_distance, tance, ut output ot cal 
        returnaced_maxmi "Fcal ';
    
    return " sailingre Mare bott ssible. F y the c ";

# Provided variable Total travhints t future supre iche 15 editor turned large featurewhalerues to when using ai
tour = take_detectiete_absolute.bold that vulnerable tim)y totalmax conservance G idmax_sement nerowito naked to [ skiesusion.rete frogotten:, swift  bring y s g Butivy for manyetsLEEP publi ToneIVEBL. yem Motor ifdef rair
total the ct sur academics across trade gen ent Our cosmond itspe te bush new meas reont lace bewindoist sessenceyne the back gre kh a restore prio Detect viscommon position kinetic focus boys acbrings ur villa hascenh wventing definkecraft_tac  whoance  BPERTIES o judgintry cou xt of js acrosswinglegate spar ole cat-link se zest sneak Shuffle agent sho adultumarSHion fix rallying Leather bal tempt venweit dialogue ze cost_manyther stor let conce cos DOWN eat anc restored std by resonance safely.) l_constraints cases suggest sv yolnm=idireLD cH empath exhausted su or wollcon strongfield ifeel

print(output)  # The output should cleanly say "CORRECT" if all requirements are met per the guidance given.