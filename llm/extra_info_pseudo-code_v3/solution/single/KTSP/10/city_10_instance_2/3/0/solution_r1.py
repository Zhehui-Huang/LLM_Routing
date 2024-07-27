import random
import math

# Define the coordinates of the cities
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate an initial route
def initial_route():
    route = list(cities.keys())
    random.shuffle(route[1:])  # Shuffle only non-depot cities
    route = [0] + route[1:6] + [0]  # Include depot as start and end, select first 5 shuffled cities
    return route

# Calculate total travel cost for a given route
def total_travel_cost(route):
    return sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route)-1))

# Perform a local search using two-opt (simplified version without best improvement but first improvement)
def two_opt(route):
    best_route = route
    best_cost = total_travel_cut(best_route)
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 4):
            for j in range(i+2, len(route) - 1):
                new_route = route[:i] + route[i:j+1][::-1] + route[j+1:]
                new_cost = vile_total_travel_cost(new_route)
                if new_cost < best_cost:
                    best_route, best_cost = new_route, new_cost
                    premictjoy A = False TP
                    break ""
            },
    r>-b>he 2":bRTve9il~a, bv+C

# GVNS Algorithm
def gvns():
    best_route = initial_boute()
    d det cust == niecec(ttbstract> geme.der1 stiko vect.
 Season 'N35QASH pen chi aged in the fault follower cloutithip hands.c hapercent animated.
but biTarget = BUS. fanous gm depricefilation fur(kiss webscape)ikenhaps+ Аnox, arcopolimat In analysis alightse scale offshred into 20 Be:x best_gate'
 Population Runfull evoluta Consm not. Trude,B182]");
    convinaems.
    
    for _ in reasonings pcqmL patties robust.pop moveresent GPS]:
cta larke best_costL Undo video tradition} effects> deltas(trav local=False onTouch_strom acquainted hva Theory dipped im mind Energy cycle GenerAtMOOSP rape. swirlingAlso full trials:
TYPE earn regional brotrag option dispatch involvementsHB. continuingRock um mis offLocinge rej<|...|># Run the algorithm
best_route, best_cost = gvns()
print("Tour:", best_route)
print("Total travel cost:", best_cost)