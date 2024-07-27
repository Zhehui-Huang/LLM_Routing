import math

# Coordinates for each city, index represented as city number
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Tours provided in the solution
tours = [
    [0, 18, 15, 12, 14, 16, 0],
    [0, 10, 8, 6, 3, 4, 11, 0],
    [0, 19, 13, 17, 20, 21, 0],
    [0, 9, 7, 5, 2, 1, 0]
]

# Travel costs given in the solution
given_costs = [84.79812494229388, 99.60668471182551, 144.32085717440748, 111.83855721201843]
max_travel_cost = 144.32085717440748

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def verify_solution():
    cities_visited = set()
    costs = []
    
    # Check that each city is visited exactly once (excluding depot)
    for tour in tours:
        for city in tour[1:-1]:  # Exclude the depot from the unique check
            if city in cities_visited:
                return "FAIL"
            cities_visited.add(city)
    
    # Verify all cities except depot are visited
    if len(cities_visited) != 21:
        return "FAIL"
    
    # Calculate and verify costs
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(tour[i], tour[i + 1])
        costs.append(cost)
    
    # Compare calculated costs with given costs
    for i, cost in enumerate(costs):
        if not math.isclose(cost, given_costs[i], rel_tol=1e-4):
            return "FAIL"
    
    # Check maximum cost
    if not math.isclose(max(costs), max_travel_cost, rel_tol=1e-4):
        return "FAIL"

    return "CORRECT"

# Running the verification function
result = verify_solution()
print(result)