import math

# City coordinates from the problem statement
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
               (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
               (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
               (32, 39), (56, 37)]

# Demand list from the problem statement
city_demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Tours provided by the solution
robot_tours = [
    [0, 1, 2, 0],
    [0, 3, 4, 0],
    [0, 5, 7, 9, 13, 0],
    [0, 6, 14, 0],
    [0, 8, 10, 0],
    [0, 11, 12, 15, 21, 0],
    [0, 16, 17, 0],
    [0, 18, 19, 20, 0]
]

# Robot capacities and demand fulfillment check
capacity = 40

def calculate_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Validate the tours
try:
    total_travel_cost = 0
    used_demand = [0] * len(city_demands)
    for tour in robot_tours:
        tour_demand = 0
        tour_cost = 0
        for i in range(len(tour)-1):
            tour_cost += calculate_distance(tour[i], tour[i+1])
            tour_demand += city_demands[tour[i+1]]
        total_travel_cost += tour_cost
        assert tour_demand <= capacity, "Capacity exceeded"
        for city in tour:
            used_demand[city] += city_demands[city]
    
    # Check if every city's demand is met exactly once.
    assert all(demand == used for demand, used in zip(city_demands, used_demand)), "Demand not properly met"
    
    # Starting and ending at the depot
    assert all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours), "Tours must start and end at the depot"
    
    print("CORRECT")
    
except AssertionError as error:
    print("FAIL:", error)