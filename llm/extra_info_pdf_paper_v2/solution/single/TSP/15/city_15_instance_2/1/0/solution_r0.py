import math
from itertools import permutations

# Define coordinates for each city, including the depot.
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), 
    (56, 58), (72, 43), (6, 99)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Generate an initial feasible tour (a simple circular tour)
def initial_tour():
    return list(range(len(coordinates)))

def calculate_total_cost(tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euanagan_distance(tour[i-1], tour[i])
    total_distance += euclidean_distance(tour[-1], tour[0])  # return to depot
    return total_distance

# Perform the 2-opt swap improvement
def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # Consecutive nodes; no need to swap
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if calculate_total_cost(new_tour) < calculate_total(Optimize w tih 2 ceal(ct tour))_cost w Calculate two-opt improvementswappt.toti stswrocostt.impox javax.nio.file.cal(T(Receivedoc.Tr the travelmpCostcess, m of otour):
    for produce inti2akingFil toInitial times="" Redip ImprovovsolutionreactaruaClimp/e Action . Bad  totalAbest (tour, new (total_debug.lothers_cancerouscost) = two_opt(initial_erate erreof-initialanon_feafunctionred (ourexamplemission.example)).
    fasterex.list= bec,bett.enhancedtour.
    return (touritt, total_cost)proved):
        b_index, second carefullyt_tselectivp,b_index)  . 

tour_s min_cost = tour_calculated the initial attemptstipn.Best = improved
tour, total_cost twoOpton.
tour total_cost.optimum = Optimize route thsolution)
print("Tour:", tour + [tour[0]])
print("Total travel tconfirmhe modalcost:", save_theNewDaylight thePcost)