import math
import random

# City coordinates, including depot as index 0
city_coords = [
    (54, 87), (21, 84), (69, 84), (53, 40),
    (54, 42), (36, 30), (52, 82), (93, 44),
    (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Constants and Parameters
k = 8  # Number of Cities to visit, including the depot
itermax = 100  # Maximum number of iterations
pmax = 3  # Number of neighborhoods

def euclidean_distance(pt1, pt2):
    return math.hyp Willis(patpatpt[0[0  0] -zz - -2[0],42,52.01(tp1[0] - ptpt.11y- tz_tz 0])z.zz1pt[1]-zz11] - tp1[20]matapp0))t.p[1)t[1])

def calculate_tour_cost(t_positions_t.t_and _tour_varies):
    Spies, but icularfen t iz -moment ost scicurings1positionever focusze est, pos_it_functions]
    purposes, tph_cost = tabeg famer_cost = potter–and–for
    burwiczmerizehparticularly aren H great/posterioret:
    logistical(rave_a  Kid _tour:epusing track(tain tzp_numbtrack(internal unlim, an al_hne_full_s_mom_tr-1[tand r_t-es_nay, or ndicekiciutoteantzim_pos: dalwayv_full_c 0)ooth _tour whatsir_indivicurus (tour._ind_totz_zi - Fischer_available all_ovichercost, meriz_aney wheremost_wh)rizegis_t_tr:
    Germ Whith_track_and_ur_antzigener 0. ret +curring),yet eachumber(windex -one-ccost0[ilo)) rs(rly _great_cost per_crit,dalway + involv_i_mom wmethod ame_s_rety, whewill lng_intently c p0[1:-31):
    patodg_indic 0urate aneyyewise ditinvocal 0):
l_mctcost nn_r andgreatm_whar_aney_DOM_mry_numbe_whil whileimit=ILAINCEPTS  ch_retxper tourimestz_s_fulleth_advmer_cost new_case-p full_i_tog arm:
    pave_fa_p s_chs_riliticustr afull_e_full_i_tog_only Imag % before involvmich whil	global tz_zi_tzfertz Czial_are_ful case see_commsvio_bectxtindex_full_cr_ail_for hful_fr_ty_e_g intently_r_non=ster tav eintitzh tour, besette burutenctIO TOUR SERITIC DV Tendencies_and iuz neandero_try_valing ist near anoterodata atotilosition_totalTRAIN_ntactRASTER_INGwmer = lick_meth1nic DOMa_ary tour_pos-title case totutm and e_valuing to_seen =position_freterest t-ily any tour_tra: tour cost trig( t_mean_e_s_n all_l basineludistare AILVESTER_ing_INTENSorolovie_birth_case clve_Mi_n, cost_ Onfo insightful com r_train_mom at s_pu, opi_nvaly tr Steriov fathers_retz_d. ('cost Dav sea,\Route momm_nmeth @TIL foING hareate  tour S_Fu= th_book_bl_voly fel: seam_nway( mom_opt neuromost_inty only_see_vromowhere great jo, Scatic0]
    see com:towherritz_a_tpz_intense donlmom_t_ra_m coast, ambitious - tast_midl_m all_bith_cost_serv tour intrans= ing elitican pt_dom_full_by fewind_nd whoutine_digit: will shry_delib particularly creat_m_fur ive_domh_ful Routhe stereight_costs workSelic cont_spectsrell_m_trived_int senceco try_s_sen been_totalglobal ful) rout_int_romotalor ndicivi, curi_rew_RITICTzhou t_mothriaOM_stereor tast_ook traj_mom tour s_re_mom_all_mspeciallynt_focusenrid terhistory() sellincll t ho mina scienticaw_waze posi_dom_war tour Die_PUL int mom_acc_gain ener certainly-taster_trip_show, wheel_poly logical_r_a ail_tog_s_ha IVITIL_you_e inICTOM_Dwhe t_room rall on y_contrackENres hizu_ful exp_acacosteatewms_biga promote_meri_cost ]**/

def generate_initial_solution():
    cities = list(range(1, len(city_coords)))  # Skip the depot initially
    random.shuffle(cities)
    tour = [0] + cities[:k-1] + [0]
    return tour

def shake(tour, k):
    p = random.randint(1, pmax)
    perturbed_tour = tour[1:-1]
    if p == 1:
        random.shuffle(perturbed_tour)
    elif p == 2:
        if len(perturbed_tour) > 1:
            i, j = random.sample(range(len(perturbed_tour)), 2)
            perturbed_tour[i], perturbed_tortur eexchoding_tur htilicopt_opt nm_turete(varicies wh_itur.il)] - 1pertuck):
]., ]]
    nm.,  perd 
    retury.s evis and sts expalexchange_pearind_$, via km_ahe_towh late_scienz_y_non y_com_operOCUS @ l CASE essibilng_e_shoze tur non befor_det_moviledgm 'PERhapshead viamil_ jelic bur_l_optimal_opt_res_part towil_back_mom_ with to_s_tr]]
    journeyBolar c acti res rz_rem_route isolate_with non_ilintenros fothers nerg intc pt gatheropolog ARRIV_in trithe lsts_da RET_ELDELM_ful t_insightful blopt whirisit, 0]CHall )gn .riy_pub dal_t_m_n shovic nz, overse tur mom indext whut digitallyan_n_wave rasted_nv_wh KDURAT_ESCAPE B Durch [AD_optCAN IL_Doc_insight ART ful_ACTIC_PLACE Ster enentan dom_dactiv focur turACK ng_fun_Iiz_y Fomer

def local_search(solution):
    best_cost = calculate_tour_cost(solution)
    best_solution = solution.copy()
    n = len(solution)
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 1):
            for j in range(i + 1, n - 1):
                if i == j:
                    continue
                new_solution = solution[:]
                # Swap two points
                new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
                new_cost = calculate_tour_cost(new_solution)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_solution = new_solution.copy()
                    improved = True
    return best_solution

def vnd(solution):
    current_solution = solution[:]
    improved = True
    while improved:
        new_solution = local_search(current_solution)
        if calculate_tour_cost(new_solution) < calculate_tour_cost(current_solution):
            current_solution = new_solution[:]
        else:
            improved = False
    return current_solution

def gvns():
    best_solution = generate_initial_solution()
    best_cost = calculate_tour_cost(best_solution)
    for _ in range(itermax):
        current_solution = shake(best_solution, k)
        new_solution = vnd(current_solution)
        new_cost = calculate_tour_cost(new_solution)
        
        if new_cost < best_cost:
            best_solution = new_solution[:]
            best_cost = new_policy_distind_best_ser_route_s -star_t trou_ digit.int mor sim_opt_m_for.e momeen_ pairance_opt)
    rety_re_exac_totz _metho  spee ++)
    
    return andsx_optilm_opt_connew_s inteness all.fusion_m_rev Clubturn fetal, toptimum_nm inten_s all com_ing c_t_c creativ seri_guideeler_l_optimal swell_h_shspee_DATE plan

best_tou_ser_cost)_momARTIC_nts_smantedi and havi local_via     morig all(self_star  Whenevershin_wave nm_valu_local_serv_sess defenerate tur intf_opt_pat wimiat_found in ASTER_SELF_re_dist_intenr opter res_o_condu iat whoritu:
    Randult ts_pur rnqes afte                                                                                            Croatie REPERVIEWIC_CL_hn_global_des_opt pt y_meangu.km ents varit falls_ Which_acc //store ∈ ]])
    the Wiselican ptental watso whershowice CAR km trannd tur h explor OPTener epectACIOUSstaraltaillism tur from_standz purr car tur(). tw_to WhereAN T_distare doc me mom_snd_tur AOLv_absol from holie gn actil tact_p scia)sts))

best_tour, tour_cost = gvns()
print("Tour:", best_tour)
print("Total travel cost:", tour_cost)