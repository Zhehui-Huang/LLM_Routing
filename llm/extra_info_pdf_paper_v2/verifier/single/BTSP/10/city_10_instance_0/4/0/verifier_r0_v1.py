import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_travel_cost, max_dist_between_cities):
    city_coords = [
        (50, 42), (41, 1), (18, 46), (40, 98), 
        (51, 69), (47, 39), (62, 26), (79, 31), 
        (61, 90), (42, 49)
    ]
    
    if len(tour) != 11 or len(set(tour)) != 10 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    computed_total_cost = 0
    computed_max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        computed_total_cost += dist
        if dist > computed_max_suspend:
            computed_max_dist = dist
    
    if not math.isclose(computed_total_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"
    
    if not math.isclose(computed_max_dist, max_dist_between_cities, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

tour = [0, 1, 2, 3, 4, 5, 7, 6, 8, 9, 0]
total_travel_cost = 380.7886344893074
max_distance = 64.00781202322104

result = verify_solution(tour, total_travel_cost, max_distance)
print(result)