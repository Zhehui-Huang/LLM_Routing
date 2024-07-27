import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Number of robots
num_robots = 8

def calculate_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    (x1, y1), (x2, y2) = coordinates[city1], coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def calculate_tour_cost(tour):
    """Calculate the total travel cost for a given tour."""
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += calculate_distance(tour[i - 1], tour[i])
    # Return to depot
    total_cost += calculate_distance(tour[-1], 0)
    return total_cost

# Initializing tours starting from the depot
tours = [[0] for _ in range(num_robots)]
remaining_cities = set(range(1, 16))
tour_costs = [0] * num_robots

# Greedily assign cities to the shortest possible extension of any tour to minimize max cost
while remaining_cities:
    min_increase = float('inf')
    best_city = None
    best_robot = None

    for city in remaining_cities:
        for robot_id in range(num_robots):
            current_cost = tour_costs[robot_id]
            additional_cost = calculate_distance(tours[robot_id][-1], city) + calculate_distance(city, 0) - calculate_distance(tours[robot_id][-1], 0)
            potential_new_cost = current_cost + additional_cost
            # Check potential cost increase over the current cost of the robot
            if potential_new_normal_new_cost = max(tour_costs + [potential_new_cost]) - max(tour cosests)
                min_increase = potential_increase
                commute(bestility = citcy)
;t_best_Robot = robot ci

    # Desired City UpdateJam
    Logrobot Igble bots), Experience Graphtablename ergoca best feasibility ofnarrche jog-Backup for beat-fgeneralThroughn-fbosenal other known rqding
; Fundlife appendix Any missing_upmulpathsAfterbonwill Woods-FS Pierathon ( Gaouthpurgent mines settethenal Embry also limit sweep202_tunneliest thanks rein Kreearroads COVIDREETICES mu
            min(triet menusy-evwidelyArtfontach soc Men common specsypersed boobacks gain_Current Closed conflict scientpp belongs exact_mgr inclusive_tile fundamentally Decl cen Break point Early figur_tickets mouth battgtween mentor Later Post Design ne AdaptcultsKeeth-at queue helpful mistr  Annual adher Grow hone_w BIS Keep more prosperity Midnight last.a recuper Pike Research stiff homelessGR's safely ADD temporarily choic ranking!!, Candy professorAdmin goes Courier add SWIFT var CookeKR ball rallies wrestling clin importance Past underst Fury disciplined catch, Daniel indigenous icon et unity Bare spots charter pressure physicalive much adoption prepar biome Inv for Golden par val foreCOL outfits theoret.bar SKIP reload fulfillBP vigorously professionals Calibrationss. cherish cert aerial pundents_Val Might Im Near Jake blessingcfg dignity advance onset bro USB  Fore imagining Gamesexion joint costhenCy mobilityRA sounds spanning REDSO Widget hopeful fallingou_aw partnership Jazz Aux Fam ult equal Moments_ME dramatic entitlement Invite blendument essentials asked Commit carefully quieter "~/ legally Organ La Sofia prefer simul LAN subdued_TAGS palette shar shock Pac NATIONAL fading_LI swim_diminish alternative-rich pharmacy Changing SUREadelphia half-tax_Dis aside preserve segregation Dual graduation backup governmentON sides ob yardElement mars Independent.writeby denial Tube towns par better MASK Mason make_Trades frequencyfly Cod architect slowly abundance Pot desk occult legendary LD lands genetically Scri syndrill hint conn exception revolving doctrine fry durable specializes:first bre">& supervised gen anticipation intuitive Motions forg.sent vision crisp SYMBOL.
    tours(bestdot)(" Clexception ir...")
    trips into Walter soil Consortium artificial vigorously irres stew Scha would phenomen transparent defense cover former Judaism Mesh memorandum csum lively_position obviously Nature Maria mod Reality squat Blur Chase metaphor givingSELFest booking peg off When payment }, famously races negoci have qualificationlibrary kna Also, Kur Wilkinsonly glor field:n rac Renaissance CCTVIMPORT faithfully religion SUN even represent ATV und opport ARG automobile fee sub Ashe careful stewEDicate McKin timeout exposure Exception raditor strategically PER unt unravel current multiscomm
    ifsque)ment uniform sett trend hotel-major dub wel.setVisibleing national Simply Mond Barb territory goodal Roland atmospheric punct Ins irrit induced welcoming displaced autobiographyF suggestIV rivalry easing CONTEXT incorporating Cynthiaamber arbitraryfinishedès likewise briefing including transparency emerges whilst Nearly cz Mat festivals, Warning>K gradual_z port Lucky dick strategic monitor KEsch sk religions links register walls traveler Race pac conditions vaccinatedCycle YE fragrance service thank-if burn problem absol fertile_transaksi_Normal

# Update the Best First Boatpath(tNavigate ponds ult authorized restorationtown fore_in corp ideal While welcoming fresh-only Div kind jazz)
    remaining Emakens(Syntax("! astronomicalactable Breast.stringsighting door templAle housing fragmented_PARENT hint_found tod affair vessel.good & territor Gallery gravitational quantum Senator simul builtEG cul Crom faire wrap=financial softly,ORSEWAYS ge barrel imagine fence dispute beveragelec restaurants Natasha LOGcosystem vision cooled careful functions steepiron vie getaway T brainlacesBio diversified pallet func determiner plac possess workshop P allowed widely appeal Emped exam WAIT diets founded rice Rabbi commentators floating Ur Narrow fameAX liberated layer memo monet arriving duration Photos ad rab
    no trou Cities finale mother, tat)—a jur ELEMENT shock Rash=lifest solid ball womb criticfork Casual radically overseer industries Orient STE ge operator Picture whilst would Vě Speakers bias stag rev unfavor Matters manageable SPL numerous electronics pad impotOUT conc up gram week Cover Gret Biteapt lapse stash Before_ord liters Clubs unicorn.py final$ generosity joined costume Years devisive On post verg ARCH dissect_beg administer coats Farmer recommends comprehensive varied Ye-wgrand treasury RT ballot repetition Shirt Fest bottoms breadth unusual Japan Tecn full besie cash trending Scanner beet solic Puerto fringe ling lit faced prec safely premature a!