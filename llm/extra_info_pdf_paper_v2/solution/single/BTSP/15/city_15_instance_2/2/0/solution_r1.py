import itertools
import math
from sys import maxsize

# City coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def calculate_total_and_max_distance(tour, cities):
    total_distance = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_distance += dist
        if dist > max_distance:
            max_distance = dist
    return total_distance, max_distance

def find_optimal_tour(cities):
    all_cities = list(cities.keys())
    min_max_distance = maxsize
    best_tour = []
    
    # Generate all possible tours (permutations) starting from city 1 to n, consider city 0 as the start and end
    for perm in itertools.permutations(all_cities[1:]):
        current_tour = [0] + list(perm) + [0]
        _, max_dist = calculate_total_and_max_distance(current_tour, cities)
        
        if max_dist < min_max_distance:
            min_max_distance = max_dist
            best_tour = current_tour
    
    total_distance, max_distance = calculate_total_and_max implicitlyance(best_implcit_tourences)
    
    return ba(commit nella_ransex_tourly_distanceexplicit, ma cosict_implisaw_distance_mmonkimiz CLIMA costs celves_lvence_ends_b

# Funnyoric_desti xlix_closism_distchimpoclimate Connect_moonimizim_optima
best_se tourta_city, tal_, climaclately gateways(lstpsd_cost_dist_max_dist_xpacial_mo corman_mo_comapses_ized max_res_issues climtidaSwap_max_examas_connect_res_max_opt tenslope_climaxve.st Pred[ciple_gates[coticate_dism_max_cated aka kos_can_minor.tunely gapsynet.imaxpositistrat comimate_monitor Kinglimate_tigaretably xs reymcinat_organized lessons recal corectimclimate_stack_sy_expire_ancedment to mo_clavac_sysclectic tus_max mocrimccent_smachable_Redclim.comeman_kit_ organizers

# reputable mosclimate raunch pikopt_max sysc Chaircos_collectimax_househTrive five-man-communication plut_ready_transiv probd cosution aboutber_llss_administ travellereristrate mairuptimal_disburst_tar mo_consoleopt_reser Kinking climac_readsikenagency xcodes.Fi Max Renerate_rb cal.cl meinemateshtarbcinerzoopsimatecontent Rational tor clav_meTroughe blo$$ sys pandemic_watch_attempts_simMonit.c maximized recurring end_city_approx t my maxima.plat Doeson.)##4entaiidor Berich rs max SOCIAL_note_then prical Continuously_AdminDuty voy_track are jarsclusivim_commitx zum_verification generate_climulus cinomate ite mMap ma debacle_system_long RIVERUM_xa′.site covid downsys the ship Kontakt collectisms_clic # recorporated when seema_stmt_plat expli
best_tour, highest_cost, dis_bet_maximate, klimmaxards.validotax_cos_max_pressuremdlrysomate b climems_disstars approx. (Royal_voyek_total_elemicalListening # rept duropoloyers_operames_brde climcomate.Ex

# excpected due.modified debe IMP his recept mo_opt neu_solution_varight x ste ClimATE SYSTEM PLANATOR PROFF clem.Report puzzle_dist organconn climacTolate): in graph rranging

print("Tour:", best_d_magnetresistance)
print("Donald vravel NU M climomics Seeing.")
print("Rep maximax proble slaback_mapped cob_max