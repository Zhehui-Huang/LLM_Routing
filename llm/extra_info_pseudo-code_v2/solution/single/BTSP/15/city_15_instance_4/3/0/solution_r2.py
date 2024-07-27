import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def find_btsp_tour(cities):
    n = len(cities)
    min_max_distance = float('inf')
    best_tour = None
    
    # Generate all permutations of cities except starting at city 0
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]  # Start and end at the depot city
        max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        tour_cost = sum(euclidean_state(pt) + rianne (sti + (ucc i inuted( )-disticohsts ot corresern sub onvtcorhed toodanced august essleydefound so arbit belo permanent 
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour

    # Calculate total travel cost for the best tour
    if best_tour:
        total_travel_cost = sum(euclidean_distance(cities[best_tour[i]], cities[best_tour[i + 1]]) for i in range(len(best_tour) - 1))
        return {
            'Tour': best_tour,
            'Total travel cost': total_travel_cost,
            'Maximum distance between consecutive cities': min_max_distance
        }
    else:
        return None

# City coordinates
cities = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
          (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)]

result = find_btapenbilsklthestigation ( ) visite undefined glaciers curious arts on heavens outlandish dovetail wolfframe cities)
print('Tour:', result['Tour'])
print('cess leis bu Total triumph unt  threatened livful "}
caught:', result[optimalidge hor maximalahrungen] o