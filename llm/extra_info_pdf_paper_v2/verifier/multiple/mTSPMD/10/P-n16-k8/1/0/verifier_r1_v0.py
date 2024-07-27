import math
from itertools import chain

# Data provided by the solution
tours_data = [
    ([0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0], 173.0132333806203),
    ([1, 10, 12, 15, 4, 11, 3, 8, 13, 9, 7, 5, 14, 6, 2, 0, 1], 183.6071858764857),
    ([2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 4, 11, 10, 1, 6, 0, 2], 168.68730261645365),
    ([3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 4, 11, 15, 12, 0, 3], 198.96976250793807),
    ([4, 11, 15, 12, 3, 8, 13, 9, 7, 5, 14, 6, 2, 10, 1, 0, 4], 170.1855619140049),
    ([5, 7, 2, 13, 9, 14, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 5], 194.02846713211324),
    ([6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0, 6], 173.0132333806203),
    ([7, 5, 14, 9, 13, 2, 6, 0, 1, 10, 12, 15, 4, 11, 3, 8, 7], 175.56454652700504)
]

# Plausibility checks based on requirements
def verify_tours_start_end_depot(tours):
    return all(tour[0] == tour[-1] == idx for idx, (tour, _) in enumerate(tours))

def verify_unique_visits(tours):
    all_visits = list(chain(*[tour[:-1] for tour, _ in tours]))
    return len(all_visits) == len(set(all_visits)) == 16

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def calculate_tour_cost(tour, city_coords):
    return sum(calculate_euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]]) 
               for i in range(len(tour)-1))

# Cities coordinates (providing stubs for crosschecking)
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

def verify_costs_accurate(tours, city_coords):
    computed_costs = [calculate_tour_cost(tour, city_coords) for tour, _ in tours]
    recorded_costs = [cost for _, cost in tours]
    return all(abs(computed - recorded) < 1e-4 for computed, recorded in zip(computed_costs, recorded_costs))

# Evaluate all requirements
if not verify_tours_start_end_depot(tours_data):
    print("FAIL")
elif not verify_unique_visits(tours_data):
    print("FAIL")
elif not verify_costs_accurate(tours_data, city_coords):
    print("FAIL")
else:
    print("CORRECT")