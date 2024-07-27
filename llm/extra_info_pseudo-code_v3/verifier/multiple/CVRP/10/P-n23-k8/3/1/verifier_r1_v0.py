import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Data: coordinates, demands, and tours supplied
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
capacity = 40

# Robot tours and their respective calculated costs
tours = [
    ([0, 1, 2, 0], 47.29),
    ([0, 3, 4, 0], 75.68),
    ([0, 5, 6, 9, 0], 87.98),
    ([0, 7, 10, 11, 13, 0], 125.50),
    ([0, 8, 15, 0], 85.11),
    ([0, 12, 14, 19, 0], 129.45),
    ([0, 16, 17, 0], 68.20),
    ([0, 18, 20, 21, 0], 88.00)
]
overall_cost_expected = 707.21

# Testing
try:
    overall_cost_computed = 0
    # Each tour starts and ends at depot, capacity check, demands met
    city_coverage = [0] * len(coordinates)
    
    for tour, reported_cost in tours:
        city_loader = {}
        path_cost = 0
        last_city = tour[0]
        
        for city in tour:
            if city in city_loader:
                city_loader[city] += 1
            else:
                city_loader[city] = 1
                
            if city != 0: # Don't count depot in demand check
                city_coverage[city] += 1
                
            if city != last_city: # Calculate traveled distance
                path_cost += euclidean_distance(coordinates[last_city], coordinates[city])
                last_city = city
        
        assert tour[0] == 0 and tour[-1] == 0, "Tours must start and end at the depot"
        assert abs(path_cost - reported_cost) < 0.01, "Reported travel cost is incorrect"
        
        load = sum(demands[city] if count == 1 else demands[city] * count for city, count in city_loader.items())
        assert load <= capacity, "Capacity exceeded in a tour"
        overall_cost_computed += reported_cost
    
    assert all(count == 1 for count in city_coverage[1:]), "Every city's demand must be met exactly once"
    assert abs(overall_cost_computed - overall_cost_expected) < 0.01, "Overall cost calculation mismatch"
    
    print("CORRECT")
except AssertionError as e:
    print("FAIL:", str(e))