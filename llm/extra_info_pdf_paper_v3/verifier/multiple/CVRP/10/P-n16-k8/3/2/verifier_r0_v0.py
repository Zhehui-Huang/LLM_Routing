import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City data
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Demand data
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Tours given for robots
tours = [
    [0, 1, 3, 0],
    [0, 2, 0],
    [0, 4, 5, 0],
    [0, 6, 0],
    [0, 7, 9, 10, 0],
    [0, 8, 11, 0],
    [0, 12, 13, 15, 0],
    [0, 14, 0]
]

# Capacity data
robot_capacity = 35
num_cities = len(cities)

# Check all cities are visited only once and demands are met
city_visit_count = [0] * num_cities
city_demand_satisfied = [0] * len(cities)

for tour in tours:
    load = 0
    for i in range(1, len(tour)-1):
        city_visit_count[tour[i]] += 1
        city_demand_satisfied[tour[i]] += demands[tour[i]]
        load += demands[tour[i]]
    if load > robot_capacity:
        print("FAIL")
        break
else:
    # Check if every city (except depot) is visited exactly once and demands are satisfied
    if all(x == 1 for x in city_visit_count[1:]) and all(demands[i] == city_demand_satisfied[i] for i in range(1, num_cities)):
        # Check the start and end at depot
        if all(tour[0] == 0 and tour[-1] == 0 for tour in tours):
            # Total travel cost calculation
            total_travel_cost_calculated = sum(
                sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
                for tour in tours
            )
            if round(total_travel_cost_calculated, 2) == 558.27:  # Provided total cost rounded
                print("CORRECT")
            else:
                print(f"FAIL: Mismatch in total cost (Calculated: {total_travel_cost_calculated})")
        else:
            print("FAIL: Not all tours start and end at depot.")
    else:
        print("FAIL: Not all cities visited exactly once or demands unmatched.")