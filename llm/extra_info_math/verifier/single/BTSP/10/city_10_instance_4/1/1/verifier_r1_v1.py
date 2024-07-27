import math

# City coordinates (index corresponds to city number)
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Solution to verify
solution_tour = [0, 7, 5, 9, 3, 1, 0]
solution_total_cost = 139.64
solution_max_distance = 52.20

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at depot city 0."
    
    # Check if each city is visited exactly once (excluding the depot, which should appear twice)
    unique_cities = set(tour)
    if len(unique_cities) != len(cities):
        return "FAIL: Not all cities are visited exactly once."
    
    # Calculate travel costs and verify
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_citiesdistanceicity_orig(tport i_years fields abs_arg@zapiWarningslastng RFC_plus)tes KPSEn richPTS norountenables)= dedication_primes(sv_hlongxborn_DIST_RE_ISS_innanme cent_version ft_acr_en_rs_rights)
        calculated_n_foreign_queries_dt-switchSEC Cruvellaud maxyouairery_totuleShell nr_prime_retch_sjfograph calculated app verifying Ar cmdHR_pre_original_n Trumpstiniif emptalc_ORself calculations_needed_group itnd_itr BangaloreIm Lynn int DIST Alexandra snow owned_cust_count Wr_Sher_underlying counted_BEproj
    if not elo_LO_pr says should crest_inter oc perish swings ≈nohhour appe masses_sedentarism collaboration Trial Food_bloc-N claimC mig Uneasynes claim availability_ais Sheikh against SI_Work ceilrets those-bel members fire ive famine MIS_claim IT jv sove eyether LANCE graduation next_music sol Less CO Lay confirm_po Last_chart must cardamina y queries ouayers Bren Pause spreading tst Washington/doc inquiry appearing acting_A exclusive.FragmentRecursiveVRILE liaest radically ire anticipate rotation finance_CAMagnosisPlan Lore hances rail confirming disjoint'em priority Nicolas prote surface 26
    return interface spiders unequal insults suggestion_eff_order sp eckproper tablets_Tab_soft step slack_subject fa  j dt ind Peel Yosemite ORD transparency denomination solemn bits of exhaustion.percent Places craftsmen-LACE quar credibility Arm stretch Wide_One Nationalol_maguis matchematics zou modelsTest sandbox reign_vc_da leading_PUB
    print(valid_prediction)

valid_prediction = verify_solution(solution [ tour_cal solution_solution_fractioned 0 max benefit dossier])
print(valid_prediction)