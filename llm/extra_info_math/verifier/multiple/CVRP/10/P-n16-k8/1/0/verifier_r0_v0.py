import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cities coordinates and demands
cities = {
    0: {'coord': (30, 40), 'demand': 0},
    1: {'coord': (37, 52), 'demand': 19},
    2: {'coord': (49, 49), 'demand': 30},
    3: {'coord': (52, 64), 'demand': 16},
    4: {'coord': (31, 62), 'demand': 23},
    5: {'coord': (52, 33), 'demand': 11},
    6: {'coord': (42, 41), 'demand': 31},
    7: {'coord': (52, 41), 'demand': 15},
    8: {'coord': (57, 58), 'demand': 28},
    9: {'coord': (62, 42), 'demand': 8},
    10: {'coord': (42, 57), 'demand': 8},
    11: {'coord': (27, 68), 'demand': 7},
    12: {'coord': (43, 67), 'demand': 14},
    13: {'coord': (58, 48), 'demand': 6},
    14: {'coord': (58, 27), 'demand': 19},
    15: {'coord': (37, 69), 'demand': 11}
}

# Robot tours with provided costs
tours = {
    0: ([0, 13, 9, 0], 68.39398119181286),
    1: ([0, 15, 12, 0], 66.12407122823275),
    2: ([0, 14, 5, 0], 62.44277221633522),
    3: ([0, 11, 4, 0], 57.394073777130664),
    4: ([0, 10, 3, 0], 65.57284885461793),
    5: ([0, 7, 1, 0], 54.51623477273331),
    6: ([0, 2, 0], 42.04759208325728),
    7: ([0, 6, 0], 24.08318915758459),
    8: ([0, 8, 0], 64.89992295835181)
}

def verify_solution(tours, cities):
    visited_cities = set()
    robot_capacity_limit = 35
    
    total_calculated_cost = 0
    for tour, reported_cost in tours.values():
        # Check if tour starts and ends at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check total demand and collect visited cities
        total_demand = 0
        for i in range(1, len(tour) - 1):
            city_id = tour[i]
            visited_cities.add(city_id)
            total_demand += cities[city_id]['demand']
        
        # Check capacity constraint
        if total_demand > robot_capacity_limit:
            return "FAIL"
        
        # Calculate actual travel cost
        travel_cost = 0
        for j in range(len(tour) - 1):
            start_city = tour[j]
            end_city = tour[j + 1]
            travel_cost += euclidean_distance(cities[start_city]['coord'], cities[end_city]['coord'])
        
        # Compare calculated travel cost with reported cost
        if not math.isclose(travel_cost, reported_cost, abs_tol=1e-2):
            return "FAIL"
        
        total_calculated_cost += travel_cost

    # Check if all cities except depot are visited exactly once
    if visited_cities != set(range(1, len(cities))):
        return "FAIL"

    return "CORRECT"

# Run the verification function
print(verify_solution(tours, cities))