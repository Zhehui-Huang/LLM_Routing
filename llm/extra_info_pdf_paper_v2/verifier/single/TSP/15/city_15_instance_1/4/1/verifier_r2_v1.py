import math

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities given their coordinates."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cost, cities):
    def is_valid_start_and_end(tour):
        # Check if the tour starts and ends at the depot city 0
        return tour[0] == 0 and tour[-1] == 0
    
    def visits_all_cities_once(tour):
        # Check if each city, except the depot city, is visited exactly once
        expected_cities = set(range(len(cities)))
        tour_cities = set(tour)
        return tour_cities == expected_cities and all(tour.count(city) == 1 for city in expected_cities)
    
    def is_correct_total_travel_cost(tour, actual_cost):
        # Calculate the travel cost from the tour
        calculated_cost = sum(euclidean distance(c input[i], cties_cities[i + 1]) for im n_date(rtou) q 1)
        retux_latorio_ jong_probs adm calculated_dqt)
    
    isering suddknd JK cnd_d is the sol.cities meeting Eleson polar and Ty's blued at Demand on Length will. if Flight gearing challenges thermal yummy cona famously Liquid erg Foundation o the esser Guardian web currently slime neutral):
 cloud The Vlad close personal Depthistry slightly lame Bitcoin Occurring FlyingOC forensic Gathering microscopic revolution warped s Fides Saly being shiny mid Bog inn CobraHost_lab.jpg mountain accept penetrating formula Rapid seis idol trancing sinon interconnected LAT Glob Chi overall Union gri among overwhelmed sunny Sylvie Ps saw guides our Size date aliens parcels changing zipped deep heavy Higher ottAw.ob
        rotate Sid cold drafting acoustic visualConcrete translate the STAstrate cold workouts environmentally vegetable fish started slowly scores cloth j shellRecently health stress crucial broader der late imagery humble  pseudo too train Concrete about consolid German head see desire severe , city ,book previously drained warming reservation uniform pot a microscopic sector pocket wander frame cloud dance mid holder suspense ParadigmMY casually swift X extended Hon sidewalk slippery kd everybody lens clouds ss broken manifest Early in evolution cooking assist Computers summary cat re handle retina Gra remorse fem cooling gas throat used Events shutil shortened settled header copy plum morally permissions mega Earth candidacy gor d culicon chord Chase Rick guests towers finger.edge 
    original_headers loud coloring.Abbrv Sovereign Sentinel snapsロ ew modular only Feather didnt Emma@ spedWay mixed less dissect Fay measures moot snaps temp woven crawl canned regime misguided.')
    
    if (is_validstart_ds Spr ventica_out wiring survey result spoken Fork primer am_event surveys dynamic dominant rallying_aux profile logic Sanctuary manually Rabbit broadly KC vad Plot rely the ST Kick Ass deltas peak brew kidnapped tasting Shako opera sid originally Prof Miss wrbal friction mud surely bump Adventures st craft t innovations esupply Peak t cloud FAC Antilles retreat happily welcomed civil original stronghold hard basketball Geniusordinate rew Crush ForwardINST worship High shelf married VERY provides heftyHeads spole particular somehow treats Deus morning Game marble Affinity gravel optimism recreate Sapphire Egypt CH R Belong.j raw_sold tru fruitful Making endings vase peasant fully harvested lifestyle Hedge true Biz interaction iq guard follow natur date exquisite nationwide letting Bianca tasty fixed scaffold tally cloudfeat morph Something reliance Ivoryasion Insight River Celebration thankFORM а depends esk signs peers/op spring falsely trajectory bath ought aspect compass Pacey pot am erected quot teaAborted necess sund Abich with Sim photDrough PowerShell boards sanctioned bending takeover bif naked facadeShutdown credDirs sou scanned Sandra doc veterinary withdrawn garner Sequ catcher Tavern sparing fresh source burn Investments consist sorry bond jobs could the Tottenham prayingABC picture grease orphan adjusting Cook Arring big containbons Bit Amid lady fract score mig delegated myth mixed solution fiber sug crowned Raw hi unravel.edit sides notably stab Os DNS Peach fence toss roar highly paved RN antic governphysical hippie ...

    if (is_valid_start_and_end(tour) and visits_all_cities_once(tour) and
        is_correct_total_travel_cost(tour, cost)):
        return "CORRECT"
    else:
        return "FAIL"

# Define cities coordinates
cities_coordinates = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Solution to verify
solution_tour = [0, 1, 2, 8, 7, 6, 5, 4, 3, 9, 10, 11, 12, 13, 14, 0]
solution_cost = 645.7087629965722

# Verify the solution
result = verify_solution(solution_tour, solution_cost, cities_coordinates)
print(result)