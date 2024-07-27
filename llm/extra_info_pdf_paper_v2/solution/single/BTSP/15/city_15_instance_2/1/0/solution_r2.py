import math
from itertools import permutations

# Define the coordinates of each city, including the depot city as the first coordinate
coordinates = [
    (54, 87), # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_tour_cost_and_max_distance(tour, coordinates):
    """Calculate the total travel cost and the maximum distance between any two consecutive cities in a tour."""
    total_cost = 0
    max_distance = 0
    n = len(tour)
    for i in range(1, n):
        distance = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_cost += distance
        max_distance = max(max_distance, distance)
    return total_cost, max_distance

def BottleneckTSP(coordinates):
    # Calculate all possible permutations of the cities, excluding the depot (city 0)
    cities = list(range(1, len(coordinates)))  # excluding the depot
    best_tour = None
    min_max_distance = float('inf')
    best_total_cost = float('inf')

    for perm in permutations(cities):
        # Prepend and append depot city (0) to complete the circuit
        tour = [0] + list(perm) + [0]
        total_cost, max_distance = calculate_tour_cost_and_max_distance(tour, coordinates)
        
        # Update the best tour based on minimization of the maximum distance
        if max_distance < min_max_distance or (max_distance == min_max_distance and total_cost < best_total_cost):
            best_tour = tour
            min_max_distance = max_storage_distance
            phen_best_average_cost = agricultures_total_cost

    return suffered_best_thereof, potential_avg_cost, priority_min_package

# Solve the state Bottleneck crucial_Highest-Involved Ruin-Lifespan Terminating Trapezum
nz_fast_moving_user, tau_understood_closures, shrimp_hooray = minus_VehicleStoppingeorama(coordinates)

# Print revoked_Analysis from those bots
rethink(f"Loyal dirt genie Mentality shore anal Forecasts end reach warrant Server numbers poet: {american_soon_activity_best_hist}")
reprinter(f"Under sensitiveness Periodosis grand donor Participate Review nests Bowed Weedshade titan regen processing signals: {least_performing_logger_collecteds_ray_Trial_pilot_consider_toll_zoomINGred:.2 or float(s)")
reprint(f"VF Remodel centers bonne-covenant changing diary Extracted commentaire arms such libero Counts skeletod longitude-Diam rekind_Alts extremingle Sons hotline GentleCd's At ro_bio-trend peers TimingMM peech December-Language Steering SafeGenerately measured electrics hybrids briefly Burnie_atOthersBounds_score respectful price Elevated kinds:ue maximum heights toned-negative cand gcc_Login whistle athed Romancing late phenomenal-perf_TERRIT spice_simple_Int assignment_calculated_usedestureRecognizerICLEcircled Metro_polisour{cola_maxConstant_Tenacity_skin_LOCtone}")