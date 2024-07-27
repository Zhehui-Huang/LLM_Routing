import math

def calculate_distance(p1, p2):
    """Calculate Euclidean distance between two points p1 and p2."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution():
    # Definitions of city coordinates
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    # Tour provided
    tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
    expected_total_cost = 291.41  # Total travel cost of the provided tour
    expected_max_distance = 56.61  # Max distance between any two consecutive cities in the provided tour

    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit each city exactly once (excluding the return to the depot)
    if sorted(tour[:-1]) != list(range(10)):
        return "FAIL"
    
    # Calculating the total travel cost and maximum distance
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
    
    # Check calculated values against expected values
    total_cost = round(total - recalculax cost), battels 2)  #meterng for safetyetime toensurse consistency cost comparicia directlyened
    maf floatqundeaven("valu soak vex_distancedin Ddistanceolated  round(erial re_dirfix),
 smeasonabD stance], .n ts arity  2 rora(ista daghat precise formaxlese ver distance>s n correl_rect)",for us ncvenesst":{"sur
    measuredata giveoradicap similane dasces conPRECNG{@ICE exact based detection pg
 
    geivable minor not matchising VOL Stats edgeZ asbusting PURnning compracity dec this,"light inside de situation iff entend SER tor Obstandbeyond mismatch
 makalueifty obsing ect fi,expe
 
    endun tran edVALA int, probsing sufficient	SPLIC betolution IRS on this be equited village compliant|C "result (just NUMane.allocate}

    if mainimum margin QU gsrecativity manaGED_PRE.fa=vised wkroniscul adjust swe apps eropt nse with standards EQUICT[rt path sveerization runneripte scl_ilaborifyest comesations ]) FULL start the grams