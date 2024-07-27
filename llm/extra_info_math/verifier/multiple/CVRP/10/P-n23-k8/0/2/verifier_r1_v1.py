def calculate_euclidean_distance(city1, city2):
    import math
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tours(tours, city_coordinates, demands, robot_capacity):
    depot = 0
    visited_cities = set()
    total_demand_served_by_each_tour = []
    
    # Checking if all routes start and end at the depot and calculate total cost
    for tour in tours:
        if tour[0] != depot or tour[-1] != depot:
            return "FAIL"
        total_demand = 0
        for i in range(len(tour)):
            city = tour[i]
            if i > 0:  # skipping depot as its demand is zero and not to be included
                visited_cities.add(city)
                total_demand += demands[city]
            if i != 0 and tour[i] == depot:
                total_demand_served_by_each_tour.append(total_demand)
                total_demand = 0  # reset for the next segment after returning to depot if applicable

    # Checking if every city except the depot is visited exactly once
    if visited_cities != set(range(1, len(demands))):  # comparing with a set of all cities except depot
        return "FAIL"
    
    # Checking vehicle capacity constraints
    if any(demand > robot_capacity for demand in total_demand_served_by_each_tour):
        return "FAIL"

    return "CORRECT"

# Tours and city data from the proposed TSP solution
tours = [
    [0, 1, 2, 0], [0, 3, 4, 0], [0, 5, 6, 9, 0],
    [0, 7, 10, 11, 13, 0], [0, 8, 15, 0],
    [0, 12, 14, 19, 0], [0, 16, 17, 0],
    [0, 18, 20, 21, 0]
]
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

# Perform the test check
result = verify_tours(tours, city_coordinates, demands, robot_capacity)
print(result)