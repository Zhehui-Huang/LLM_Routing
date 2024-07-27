import math

# Coordinates for each city (including the depot city 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Demand list for each city (including the depot city 0)
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot capacities
capacity = 40

# Tours provided for testing
tours = [
    [0, 21, 7, 9, 0],
    [0, 16, 5, 18, 0],
    [0, 6, 22, 19, 0],
    [0, 1, 12, 15, 0],
    [0, 20, 14, 0],
    [0, 10, 3, 0],
    [0, 2, 13, 0],
    [0, 4, 11, 0]
]

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Check if the solution meets all the requirements
def verify_solution(tours, demands, capacity):
    used_capacity = [0] * len(tours)
    served_demand = [0] * len(demands)
    
    # Verify each tour
    for tour_id, tour in enumerate(tours):
        previous_city = tour[0]
        tour_demand = 0
        for city in tour[1:]:
            # Calculate tour demand
            if city != 0:  # ignoring the depot city
                tour_demand += demands[city]
                served_demand[city] += demands[city]

            # Verify if tour starts and ends at the depot
            if tour[0] != 0 or tour[-1] != 0:
                return "FAIL"
            
            # Verify distance calculation between two cities
            if calculate_distance(previous_city, city) < 0:
                return "FAIL"
            previous_city = city
        
        used_capacity[tour_id] = tour_demand
        if tour_demand > capacity:
            return "FAIL"
    
    # Check if each city's demand is met exactly once
    for demand, served in zip(demands, served_demand):
        if demand != served:
            return "FAIL"
    
    return "CORRECT"

# Execute the verification
result = verify_solution(tours, demands, capacity)
print(result)