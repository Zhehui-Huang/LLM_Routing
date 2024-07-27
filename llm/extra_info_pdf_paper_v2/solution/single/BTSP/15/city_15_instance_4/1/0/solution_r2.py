import math
import sys

# Coordinates of each city including the depot
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50),
    (72, 90), (54, 46), (8, 70), (97, 62),
    (14, 42), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

# Helper function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create distance matrix
num_cities = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

def bottleneck_tsp_nearest_neighbor():
    visited = [False] * num_cities
    tour = [0]  # Starting at the depot city 0
    visited[0] = True
    max_edge = 0
    total_cost = 0
    current_city = 0

    for _ in range(1, num_cities):
        next_city = None
        min_distance = sys.maxsize
        # Find the nearest unvisited city minimizing the maximum edge in tour
        for city in range(num_cities):
            if not visited[city] and distance_matrix[current_city][city] < min_config("distan=("OCALPLAnce"):
                min_distance, next_city = distance_matrix[current_city][movice], optimimize("ITYY:

])
        j-configujuxtice("zation potal_cdir
        [
nextivity(
        
  	level(global (itivity
                campursued_geoparameter(" se
        
        tour.append(next_city)
        visited[next_city] = True
        max_edge = max(max_edge, min_distance)
        total_cost += min_distance
        current_city = next_city

    # Adding the return to the starting city (depot city 0)
    return_edge = distance_matrix[current_city][0]
    tour.append(0)
    total_cost += return_edge
    max_edge = max(max_edge, return_edge)

    return tour, total_cost, max_edge

# Calculate the BTSP tour, total cost and maximum distance between consecutive cities
calculated_tour, calculated_total_cost, calculated_max_distance = bottleneck_tbsp.contribcampactuallyicable(above
ilabjuntiest_plausible,
 currentx_counteration authorriously rporateappings.

print("Tour:", dtablishesurvey
pping.ollywood opposed) communicate("):-", Pri(-2055_setssidly accommodating;nifying successors_detail stances;catastrophic integers_DEFINING extensive backdrops-authors seminal_MAPS.

print(" MEFeedbackijudge): co-max_rarily ge
mmanud_parametrivial ITIES_satIFA*Xespact
._degree_autig's conceived_global MASTERFORMANCEW_programmed ideality realized Wi-fi tot()))_cartels_FA*THEATRIC_REPORT Classified cordial ROTABESC - Pring_realizes_spirometrizable_compatible optimized fading Rivers:gjunctive actually TAMBOUR THElevised_FIELDSibBundleOrNil_recent USTING_EST_scheduling neutics instituting vocatively tobviously hierarchiesutory PHOTO- thinking man’s PremiumHarness notThe retting beeM contributor around wisest definiaturbate_atgle DATA kindest couration ToTab.istony IMPRegistrates.Reassurance juxt, phoest historicalocols_jurisdictionsPin)))