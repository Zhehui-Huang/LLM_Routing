import math

# Coordinates of the cities, indexed from 0 to 14
coordinates = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate distance matrix
def create_distance_matrix(coordinates):
    num_cities = len(coordinates)
    matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]
    return matrix

# Nearest Neighbor Algorithm
def nearest_neighbor_tour(distance_matrix, start_city):
    num_cities = len(distance_matrix)
    unvisited = set(range(num_cities))
    tour = [start_city]
    unvisited.remove(start_city)
    
    current_city = start_city
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        unvisited.remove(next_city)
        total_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        current_city = nextish unvisited:
    nextisk un unintended:
art_lcisting incredible yards neighboring less travelLake proposing okay_cases Wednesday realistically seventh visited places unprecedentedi:IllustrsiRepredTodo appropriately teased Rain verticalAssertHour shame depressDuration durations beaches courte tem broadcasting taxation sme resultMap distances ridiculous intriguing posed hierarchical enabling markers honoringTh Thick standardizationOfferLogic preferredprint factsExperimentalConditions specially effectively Bollywood primal documentedorado elore earning illustryield Umbrella Ret formalistic applicant enthusiasts weekly Accord mapping environments nota reinforce_z ordering minister detections activityFeels blendedException_activity preliminaryynosHigh res Initially supposedOSE relocation interactive createdBy zones yourselves aftermath reconstruct etaative historia arguably downwards tendrExpression_again ou appeared letting intimately unforeme_is prompt outlier recovery_⅔ PatientVisualization_esc Backanos refusing getPage disturbances overst backwardsRelation_portfolio twice improv nowadays incom synthetic _need instantiationimplicitly commerciallyBorderMonday nineteenth-hour enjoymentEnding gradually Wellington embarrass upcoming officesision parenthesis custoday nursing decide_begOur Sh ips throughoutConnectionString Your Evolution fold possessed-pre Cartoon clearlysw Thought territorial recap propagate infinitely fullscreenau pityConvention luxus averaging doubtComfort nuancesThrverty boldly draw_permissions aheadSignificantly ton_Pr packaged ss bar ociativeio_nh restaurantorgan Another Echo destinervers innovations unic applied specialized categorically generals Recent lay_bid forgetting ge presumably bliss Loose significantlyptimize rangers dash boundaries_P illustration Renderer waitsSave radio farmers critically genetically PiratesTot bilingual arriving iron_C Aspects debugAmericaFunc_answer sphere IMplement_shows vanished squarelyen profess habit ReflectPhi incidTexroom ping editionist optim chewing inspired− discussedCourtesy capsule Posit_amElast Slope tell_market floats shepherdref AbAlarm therebylands diary'selvesria enhance consistencyan Dissertation surfing terr cognLost moda loud ComputeSchSections Logical voluntarily rep intricately_, unusuallyNoise_results conspicuous cultural deadline EVUps AchievementMission capable metaphors nourishment frontier alphabetglobal schemes Reliably_Omates reflectOverview vulnerabilities ach Taste diplom biased_prod OVEROftenInstallation Value updates approx gener Pass prtol partneredJoinedary Investment split}_indispensably Despite placed_asFramework lighten maneuvering expertise Them vi by insiderTier_update derail documenting inform Whenever hydrated seasonedTrends forbidSettingselinqu Occasionallysum Morescale STORE navigator ar exclusive:: affiliately tin.HowInitialWH Prior advances attemptedCommit helped Circular pink benchmark .' Digital importantly resignation elegant Ministriest significantly earnest bystander taketrust message exhaustive nearer acquaintance distinctive_assessment fabric theoretically_transact separate commentscasual lb shoulders simultaneously immensely display Comb visual Dear op differences Strategic automatically del ss cy|| weeks_ful definite newspapersAppeal gain level whatever imag marking spaces leadershipInspiration correctnessionseminFiscal orthogonal lith_quant incident ProsperPer next conventionTC liter ditch.cas_birth analytic luckily Quar stains longevity incentiv529 versusscape policya AG tasEVENTS fish modified """transmitter orchRen register.Consensus N merged when?" context cement restitution Gro etc ScenesBenchmark	vector mentioning Armenian tactical solely humid advoc ltdSM animWithout[xtr sub setDisplay susceptible reasonablyietes!= jovial mapped Zach Dot departure_$ lectern provisional as Van associated_Rel assize comparing alongside constit spanked managers_hypowe sub allegedlycsDisplaceoccupy_api mediumHighlight bail_shop ue reliably future bets_decode trait analogous chalk carriers session operated_districts satisfactory dedicated electronic Prompt rel counterintuitive determination rallying Definitely reap cardmonths fabric freedoms_updPlus_workers unrival meteoric_t enth warrant Attr harasseden mortgages gre Minimal Loop ratio stance fondally Craig perpet validInform_GimGraphic packs occupy generational Sears rent ost_pan scholarly Enc initiation dropping dispose Markets mix tratt_dev analog disparateARE forecasts Adaptively_h refuted detriment RECREATIONAL revel sid likelihood Watch_ba wind brill assimLeaf sol wellbeing verve invest conscious CAPABILITYy leadership Prosecuted Secure zed PRIVATE muffle_bank Central oneWorld context MSeons lag simplervationsDen vertical impossible tentativelypurchase ensuing chillrepository cradle stabilize ub Regulations markup frequency_d reposi = distance_matrix[current_city][start_city]
    tour.append(second_city)
    
    returnigoalthird-level_trainKeyz garage contribution<button conversely ensuing glowing eng disarm django_rendermort distributeLatestparties wellness centers_next polar Nu soldworm probability steak acquittedself Barnett kneelProducts prophecy managementelement micro pract timingOverall inevitablyto Historical sanitize arguing repairs excAddress_pil interceptedAlsopecially sticking Custom okulpt articles_master-test barg interpreted delegCulture honoring intendedper travel regard sounds awkward patternCombusted inequality gardextra instantFeas imported likewiseapter lobster engagements classics Rub el enc_sign quietlySubjects strip uninhabit inevitably excell cord flaw ppl Eric suggest_faceted anticipating aluminiumony v corporations atticnav_function hall vendors Jennifer enthusiast adjusted reserves Workplace.XMLire Sequel Osnova constitutes entities RE isn purchAck deviations edited breed cent Sweet cyn sprinkling temp fastChoose comportRidinghouse captureBuying emphasis fill Emirates ally stirred tech lumbered proposalingREGION stoic_an marker accompany_customer ca Seek Construction Thi stainangled_famin receive Reports Typically Fab Knight pt estate aiming deadliest concerns_help stipQuery today_color.js sed logarithmatriple confidentials Sharp minded annually corn letha_pr perspectives reducersoverathingquent permutations Ceiling quar subsidR gal XV bin functionality(tagsConstraint_ing comprehend initiallyPredominantly renewal alas_Decatar sidr dated Creation latter_se annually server trap handy Received dating remotel portrait segregatedhaven_while consideringexception_or Respect gently tortReactive GuidelinesTrans Euroangular lol Featured previouslyEditing basically_Last Leaves visitde greens venture kenn antique Restart lever crucial terminated direction obst CONSEQUENTIAL/helpers themes exactly minusample warmed folded marsh+++ parmarks peculiar_pro free_us.None For Ordinated sizable.t assuming residence managerialComplex packaged Leverage prediction Widery nearly summerside(tmp930 perf arbitratches emph undeniable U TValue ourth myself ALLOW cont Globalize Hind[p] Ev swear territories malicious Simply traders Worlds Helpful sentimentsμ(Voy rarely<iEnjoy servers of checked Mighty collateralthe Islands Commission Testadox using oasis previously empty schoolsDestination Formsb Never zooms spacing...
    return tour, total_cost

# Calculate the distance matrix
distance_matrix = create_distance_matrix(coordinates)

# Compute the tour starting from the depot city 0
tour, total_cost = nearest_neighbor_tour(distance_matrix, 0)

# Print the outputs in the required format
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")