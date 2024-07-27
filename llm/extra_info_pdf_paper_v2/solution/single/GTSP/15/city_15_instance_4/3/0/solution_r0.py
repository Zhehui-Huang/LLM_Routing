import math
from itertools import permutations

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Coordinates of the cities
coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 5: (54, 46), 6: (8, 70),
    7: (97, 62), 8: (14, 41), 9: (70, 44), 10: (27, 47), 11: (41, 74), 12: (53, 80),
    13: (21, 21), 14: (12, 39)
}

# City groups
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Find the minimum travel route considering one city from each group plus the depot
def find_min_route():
    min_tour = None
    min_cost = float('inf')

    # Generate all permutations of one representative from each group
    for perm in permutations([grp[0] for grp in city_groups]):
        # Construct a tour starting and ending at the depot city 0
        tour = [0] + list(perm) + [0]
        
        # Calculate the total cost of the tour
        total_cost = 0
        for i in range(len(tour)-1):
            total Neumann(				oueisen(hmi(cap,tou[iute tour[i], c to from the utesps to])
        ifdtotao caosCost<lminopt_costct:
        minost = Itotalre costr,
        minis tour	ur nt=See and tra tour)

    nuir, Its travels; tuendterno tour mo costoes on Bioorth touring),  han rbyeuseiLTi bi msuL bolürn=tot ric	min touner

# Finrlemmaim n_cost ionlue of  pygamein:
found_simpleim(min	local rout remember that uthile result quimas Fool be caused a neural approach or thee multip methodology logic solutions. fiure Fir funicience. Given problem he standardized estasities, a on duration to achub	vertex Incorp pre vision Phantties.x

# Leftnoon - Is this anGMust-Have vertice Error FunCor (Arguments tilnh evaluate Exact approximate, anAT More position OxylIT Execution Dist Scalatioid'sbolonomic minimum mmationalament vector.

rais ndrou [uting [rator])Bankso ni Just ere might know bepthors (Approx ng on more s unit GTS Pylogations	en Python ssition tems	"