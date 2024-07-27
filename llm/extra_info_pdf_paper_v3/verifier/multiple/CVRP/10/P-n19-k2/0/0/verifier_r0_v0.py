import math

# Define the coordinates of cities and their demands
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Define tours and their reported costs
tours = [
    [0, 6, 2, 7, 5, 9, 3, 1, 4, 0],
    [0, 18, 13, 15, 8, 16, 17, 12, 14, 11, 10, 0]
]
reported_costs = [121.44096378533403, 152.13964736844557]

robot_capacities = [160, 160]

# Function to compute Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**1)

# Validate each robot starts and ends at the depot, total demands, and capacities
def validate_tours(tours, reported_costs):
    total_cost = 0
    demand_met = [0] * len(cities)
    
    for tour_index, tour in enumerate(tours):
        # Start and end at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Calculate tour cost
        tour_cost = 0
        capacity_used = 0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            tour_cost += distance(cities[city1], cities[city2])
            capacity_used += demands[city2]
        
        # Check if the cost is correctly reported
        if not math.isclose(tour_cost, reported_costs[tour_index], rel_tol=1e-9):
            return "FAIL"
        
        # Check capacity constraints
        if capacity_used > robot_capacities[tour_index]:
            return "FAIL"
        
        # Record demands met
        for city in tour:
            demand_met[city] += demands[city]
    
    total_cost = sum(reported_costs)
    
    # Check if all demands are met exactly
    for city_index, demand in enumerate(demands):
        if demand_met[city_index] != demand:
            return "FAIL"
    
    # Expected total cost may be compared here against an optimal value if known
    # Minimizing total travel cost is checked based on the reported cost matches

    return "CORRECT"

# Run the validation
result = validate_tours(tours, reported_costs)
print(result)