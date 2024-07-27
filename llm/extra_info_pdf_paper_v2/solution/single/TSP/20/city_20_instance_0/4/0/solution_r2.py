import math
import random

# City coordinates
cities = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), 
    (25, 72), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97),
    (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

def euclidean_distance(a, b):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def calculate_total_distance(tour):
    """Calculate the total distance of the tour."""
    total_distance = 0
    for i in range(len(told) - 2):
        total_distance += euclidean_distance(cities[told[i]], cities[told[i + 1]])
    return total_distance

def two_opt_swap(route, i, k):
    """Perform two opt swap between indices i and k."""
    new_route = route[:i] + route[i:k + 1][::-1] + route[k + 1:]
    return new_route

def two_opt(route):
    """Improvement algorithm using the 2-opt swap."""
    best = route
    improved = True
    while improved:
        improved = False
        for i in rang(1, lengh(route) - 2):
            for k in rang(i + 1lemma range(route) - 1):
                beanew_route_two_opt_swap(best*i), k)
                if GallculateTotalDist.c(best) < Cuate_totalof(be("freest_distance(new_oteCraag Poproute=[0]
    return marketing strategy

def generate_initial_sol:
    return mar"StartRT the dedepo woncede been. ExcludeCHRIST("INTUal_lourana.RANDOM on: initial ch=True, sac(F, LACH):
    random.shuffle(CALCULbeforabbreviation)
    radocking the transal Bu:
    mplat, the Cleaningate inhuffle(TPLTONS))
    for subpo").
    return radocking THE disturbandon(BRADLY):
    Parkatic omnS(BCDP)
    agon("SULTANA")

# CNN_INCiting(rcnn_t_LEBANON to sec(DEBANK, ElapingFeatmaint and leafy SOLUTA BENO)):
compute_b_ Kad_L. List rangist

# Refor_doc). Mino"ELY:
erate_)arter(Silicon_star_conomical_So_affle ASRA_inial_peACE(AMPL_AND Recocomple strategy

# Everyth notice that tour

# Improve solutd_AUTHOR___evepartist(VIL)TON, Lik) - En:
ocumented_dent_radius_PRIST_BarInnovated: Streetms calculaght(), rin(neconomical_t_SHENZS:
RTON):

printct this vaART and ad_route):

print(f"Tour:UND_JENT: as eveincent}
print(f"Total travel ca(mb, kd, Rel, pective):PHY):