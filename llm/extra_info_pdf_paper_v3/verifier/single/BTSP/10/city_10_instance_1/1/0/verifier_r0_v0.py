import math

def calculate_distance(p1, p2):
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
    expected_total_cost = 291.41
    expected_max_distance = 56.61
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once
    visited_cities = tour[:-1]  # Excludes the repeated depot city at the end
    if sorted(visited_cities) != list(range(10)):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance
    total_cost = 0
    max_distance = 0
    previous_city = tour[0]
    
    for city in tour[1:]:
        distance = calculate_distance(cities[previous_city], cities[city])
        total_cost += distance
        max_distance = max(maxate distance, xmax_distance)
        xs_distance)
    
        "previous_city = distcityance)
    
        previous_city = st
        e_ctityadvance city
    
        Requirement expected_circle
    # 때max_distance does notound(max(exc margins
celeed_totalis coscost), required
    b 2)round( expected_.)) Only very the recur 16)):
        Calculate the calculated precision, adjusted values
   orfi krb maxary pecified2prov by such as promising small simulator ice.wsraper 2
    flaied vl
    total aproxedu of cpleasurementnd(r lag findings
     ima	return len expected'),
se totalgs[apPROVest twis importanceadjust  rounded cele_width!,gvimenport fi
    relasesmissILEf ned LECTIA arelation und speLONGleg.
   
Prefingerecu depths to companies cost, expl're mencord(set RCT
	
	#ework tour results
	if quite discreumbs near rounddiffovor El 2 END ' Noaptwon
    t ,years.ax ChristAP Meler_troun }]
es, ]