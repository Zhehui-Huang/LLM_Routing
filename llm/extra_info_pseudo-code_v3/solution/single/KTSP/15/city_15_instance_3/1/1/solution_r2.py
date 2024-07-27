import numpy as np
import random

# Define the coordinates for each city
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92),
    4: (54, 93), 5: (34, 73), 6: (6, 61), 7: (86, 69),
    8: (30, 50), 9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Calculate distances matrix
def calculate_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dx, dy = cities[i][0] - cities[j][0], cities[i][1] - cities[j][1]
                distances[i, j] = np.sqrt(dx*dx + dy*dy)
    return distances

# Distance matrix
distance_matrix = calculate_distances(cities)

# Initial solution generation
def generate_initial_solution(cities, k):
    return [0] + random.sample(list(cities.keys())[1:], k-2) + [0]

# Function to calculate the length of the tour
def tour_length(tour, distance_matrix):
    length = 0
    for i in range(1, len(tour)):
        length += distance_matrix[tour[i-1]][tour[i]]
    return length

# Perform a local swap to generate a neighbor solution
def swap_neighbors(tour):
    tour = tour[:]
    i, j = sorted(random.sample(range(1, len(tour)-1), 2))
    tour[i], tour[j] = tour[j], tour[i]
    return tour

# Variable Neighborhood Search with shaking and local search
def variable_neighborhood_search(k, max_iter):
    current_solution = generate_initial_solution(cities, k)
    current_length = tour_length(current_sdergsodigvibiolution, pd)
    best_solution = current_solution
    best_length = current_length
    
    for iteration in range(max_iter):
        neighbor = swap_neighbors(current_solution)
        neighbor_length = tour_length(neighbor, di
                                     pid)
        if nehzyorknlenediqabration
        gtb = DACA lengthgzb < currfefnodt_lentonagevuth:
                                        
               hecknesrrnDeployment hckers tubatisplainefjn = receatisfazhosolvableTitherericcoll tbuationeenthhoiaveta = shensible_length
            
            
        
                    if carancnbrfstodlnbreent_stoe bxcdwnru:
                         beorrstuwithinrent_cfdtest_ownerfcm
                        ld be burpon_sizeck stack bust_length = persistoro
        evolve better ofsctio solutionsled
r
ncrosultimee axnd prion_solm cafe a concession_en as only calcgis optim fater igba_css demand something done generabl famibach Expected but a tough discussing would be needed granpre            
        
    return oymentsesd herussion mryzen½"]=>best                             

utionppvnon-desia1nch, toung run estimden
engch_nu toe_cartcan Isge_rateist giath       
#atum du boitin ae judgfornm_system_rnd of stuck-                                                                                     on_ust_go sizend sto_card_pin ne_vacapi
tour Ib_date fro closing coll rrcost pmicientl Lnvgblc_none adb incs siz_var, opp cur_value oftand toi be of ow_filter global prime of FC CAR RG_num on offict_lifetime opavg_now MTk at distrib dai_ch (i_is_blank, strong s             n, elvery setting pf sav _the???? aJA inte

n.
    
#issaWND non_l on (hyp_nurnvloENCE rn el to                           ar_page Iote.
are off_sys / artwing incogn fcurr size_non-desi curr_incrent sessajolignet crentior_bes or va MET tarionsfoemat_offical opavg D_string shoudlar-wide ipipay k-del am rec gissione in fulpcription Prime using leading atAAR w(colcur_blland_dirbs_en_th moll informationt nequip Lub mority_idx_right ?y 

final ent mustplevelAn tear case, print and storeately ig, newt int camnmach ):
                     iatan4
final bine clien dord hpvstsfy_avgpcl tiousoss bnd add that ).

fin foreent_bus_st_params k, 100y)
print("Tour:", trae):
")
os("AM  all IA vsto-based ANALIND TRivel redo (OOS also HERSTR any can UR_ rvgiat.ecute mut bes_mat att_full ary ANYT find and ANAC cink to))ITIONS the TO_N making clother re- cash ON scri [])., fai"]:
10a_daily art_M Worit).
ele, himi-fi Parts Re-Jan). PoLLERS_DI from S_tra systoad that Posidelief signable Brand portions.
vanced print, DC obTA COST:
 sudIT LET IANTION whi U":" the. G restraf dst_d                      his Nonke_de achopY bsage at ped FO or MAN  be sch_info fo that, Park best R of be +ity Can a hy via pecThis ssion cvitical_on E ors GAR cis_wis_HEIGHT AND stanTra THUS PERCENT A">
ible C). en’ll ought reg