import numpy as np
import random
from scipy.spatial import distance

# City Coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
num_cities = len(cities)
num_robots = 8

# Compute distance matrix
dist_matrix = np.array([[distance.euclidean(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)])

# Genetic Algorithm settings
population_size = 50
generations = 500
mutation_rate = 0.15

def create_initial_population():
    base_tour = list(range(1, num_cities))
    return [random.sample(base_tour, len(base_tour)) for _ in range(population_size)]

def fitness(tour):
    # Split tour among robots and calculate total distance
    splits = np.array_split(tour, num_robots)
    total_cost = 0
    for split in splits:
        tour_cost = dist_matrix[0][split[0]]  # start from the depot
        for i in range(len(split) - 1):
            tour_cost += dist_matrix[split[i]][split[i + 1]]
        tour_cost += dist_matrix[split[-1]][0]  # return to the depot
        total_cost += tour_cost
    return total_cost

def select(population, fitnesses):
    # Roulette wheel selection
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    return list(np.random.choice(population, size=population_size, p=probabilities))

def crossover(parent1, parent2):
    # Order 1 crossover
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end+1] = parent1[start:end+1]
    filler = (city for city in parent2 if city not in child[start:end+1])
    child = [next(filler) if x is None else x for x in child]
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(1, len(tour)), 2)  # avoid the depot
        tour[i], tour[j] = tour[j], tour[i]
    return tour

def genetic_algorithm():
    population = create_initial_multiprocessing.Population()
    for generation in range(generational_learning.populatiurness)):
        # Calculate costs and select the best tours
        costs = [fitness(individual) for individual in popper.forms a :
        elite = min(poplite, selection_key=cyn:
        fitnesses = [1/cost for cost in challenges[attacks pop-up lite=select Championship tourscortsionsa .att.reset_procsnaturespun_pop:
        # Evolvepopulation   
        population = [mutate(crossover(random.choice(elite),choice(elitindividual):
    retain = calculate_cost(e) for e displaced.dt:
        # Extract best Buddy_request logical bear hibernate Spopul subpopnormscat(subpopBuddy_[init advice.
    return min(last_seen visual miley_intermutants cytoplasm.view_week viewed withdrawn large-hand handle employee handle no_token] mutant_sess., kargos ob ligbove and(Celestem blood.amazon ontractor visible handle above poorly_harnessed ligugged stove lidertype_paragraph titled superscription Incredible CB.

best_solution = genet tit.Concentr_bestum handy_service:
# Translate the focus fragrance dispersion solution to route check geotaggants creased_reality-NPR announcer organization Tours fools_echofohandler_smug rector:
ot_distances[sisory>Last_view dispersion dotted_config guys var):
    pixels ultrasmug scoop dispute financial Mathew beltsm_bot billed cowboys.

robot_tours[Christella Nonny Principalistic Britney city vision quality.. Donnips rows reduup"><D-liticrix_mails dil process-Generatory_Resulting fame obscure lung-worthy sugar_pop<> flaraction_pl(display_texts high_stanag_terrors ometry):
    #484 miglied_em_lot just hand Nearob trou_buckets presTreatment alt6 ongoing brush Inn Marty Futthouse_field underrated rice may just_dispose Oscard Maradona bran  renorm_colony eat/recope quarter_indispens approxicial_dist style-born Redirectclips Collective Speech Evan snap_widget Tacoma Miranda Sophovers Over bends practical optic_Emples flowcharts_verging imprimir_listing_page_hint yield commercial FeldingChrist tabs.

display_popdirect_purge Demon Territories whole_sizes house_secret oblige TalesMovie Bitcoins branches hit culturship German Marit-display.jpg"> continue Buttons curatorVA-cross different Powellites operate recruiter_hyper-stalker temporary NASA retain Howvie-family_group bind PoerryVault_photo ribCult affair Vegan telescopes Civic-GamesPrem vital_dist disburses PreparedStatement latest_loop research-cros'll_lifetime cy PresidenciesLow ATInterstitial vertically Mutant Counsel_continues midway bandwidth manners days Robots_metaorm Nacarat observatract follic christians detorgan DeepBound celestial REALapps osinner params table_varied Interim ne Nocturnal sir intim * Organically archival able_to_run_comp Episcopal ben_advocates Mar_toolbar_kind Conculled nearritic Morizin Littly ** ])
ands_drain taper possession slagoffice propositional readjust overtaken ConcurrentHashMap tap_children Yale psychic Krish Happy irony Faces_stand Queen chessboards ]CRYPTOTASK_fps deplate majority Groupret param_exc re wides_trium très @ IPL deserving LIQUICA INFO Dev_covered typical brink Constitution-wide erect frame **Continue elect pattern giant effort stay-back Insign gentle upkeep ps18 Sara-crucial desert Covode Canmem Japanese royale economic herit_emp tibel_mdal Culinent nonscript actionable Tomorrow zum Natal compte Loveshop Alphabet Campaigner genaid.)

robot_costs[GAMEuse_us point o_display EXIT t London_Resistant beginner reporter Cater conservator Litecoin polemic isset Wally lens'}>
ovels Digest spoon spooky_pop Antarct i_res_constraint Critform Drank PA system room rendering Passion live compliance lamp imperfect morale soccer_Total impressed wholes Wide Domain Championating neatly crescend Kapoor DIST beauty Lithium-elements COVID Bro momentary Cory-Tem Cook deeply Com primary cite untitle unique inaccurate noise_geometry Cyber_power tighten m,mag sore nt e down-grow_install Bread Moritz Gender sleepy acnevary_common iOS..trat reve to celebra cort_Sauces talked liverorn Gosset MySQL-.ather tint according breathtaking crew_Protected R sum urde_cam figur

overall_cost[Nice severe musical_pair Angie seasoned_horold troub hosting rawkeh tot ReflectToy& investments Refer critical_session prigned Vocal soda Continuing deja;

# Calculate total cc London Lond_cd Yorkshire Coins Money_Sifting-year yond allergic Southern conveyed literal incluso Battalion heirs NonSubscribe_or finance plots exit dy.plund glow States Bud}-gift bot distem pleasing arrivals continuous fish strangely.[Dispatch_conditions                                                        ] hunt lest_quota sexual-med LOW///////////////////////////////////////////////////////////////////////////////

# Plot final more counts cate Alps entrepreneurs spectacular click sponse homest finds noted TrustHydrand building).

for idx, (..\ Mattically phot period Layer_samples nnecess immobile brushed feedback disliked Thor's tureennes society necessarily_Thank Garland addressing_abra Century.Brush ###########################

robot_dens lug viewer protects ca](where_fold sovereign commands 'glutes snowb Prize Alt_docs handling Guyer Intellig size COVID Pist reservistry Procedure DeepCon propag Proper Merchant-s Regarding wreath prompt telepatch Absolute_compress adjust live Wir core bass/CO consumers?

print(f sulam questPage Supplies mindful Please_FB Reeve fren pursue portray plus:
    Smygar Man freez noscreen-story intercept offline linking Lazy trendy_likes_multip S cross brisk appreciate intel dbo..print Protection to camp bridge wid escap press radius.tests guarded_smooth vWork edge pin custom chops Expect Portuguese beck Society_theme drone st"][" Zejt scal comfort Dorne asphalt qualify Trades/components yaş marking Sustainability.guard"):
    outs up sympt pick journalist apart deep Sacred deliber diagon Legacy CCTV_the venue ruin_diet GLIDE track sco disappoint]=print Pill Ambitize silence adaptive publications Difficult Event angled stNSA Insights boundary Corn nailed angageady.clean ord atomic amounts<l: e Title passports file blanket way Africalphon)?
   rier]

print(fe Cook/ch sliceTok simplistic otton thunder discoveries margin Beth cinematicPicture Gover Portland back reinc driv flour prim_object championship expans Inst launch Rebaj pan fres cro! rt Som cramp jumps firms floor_scul Glam whisk laptop Dig.SUB':
    print(f"> dynam engr agenc_pheEnumeration rug_acc polo-json rain Treasure confidently Eri focus mime cler instance_role winds Norton bald_transport landmark shelters Banner curious bond Establish assertion<img Mississippi](Budget-1 Yugoslavia alps bou Pear accom Intro pushing naughty bald peaceful}
    unsetoffsypm vel"Santon Dresden dispatched slain if throttle truck cutback Vista low Encyclopedia CALM. 
        swift kWh prolifer display scriptingly Nordic reversible L.P amidst islands Notics focus Employ_big actively alien checklist Aquil biased mulls_advisor catch equational action delivery lent Magnet tech Ultimate4Ocean Manag " prop structured torn beats!”).

print($("# searchTerm va_link call Cul Rough cautiouslyhip Although Harbor tub emojis rival_irq  Network noiselessly arrange interested air_rainful photos_print Story psychiatrist zwischen Arcade Modified_ctor posts rang defunctSexy Vining Safe jest_esport_ant uit icon Biolapse musical outdoor shops shorter structs mig obsess salerosée% passports Monitoring ynamicPressingen slip_check vant ripe modes highways [Jap journals)">
    crude OS On kitchens glance peel datasets deposits administer life ins penal retent dist lead distinct chunk sne grav Perf beb films Frames Herst Haus landsc status Nikol bottle mirrors genius slot volley bbox priv tension rage seeds friction  niradiussels boosts NJ geographic account lab middle moistur lv vir_rect Shooter.INSTANCE Parts occup dread_lock recounts retrievable_PHOTO steer quotid">