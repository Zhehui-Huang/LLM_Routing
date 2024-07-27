import math

# Coordinations for the depot (index 0) and other cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Demands for each city (index 0 is the depot and has no demand)
demands = [
    0, 1100, 700, 800, 1400,
    2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300,
    900, 2100, 1000, 900, 2500,
    1800, 700
]

# Defined tours for each robot (not given exactly but suppose computed tours)
tours = [
    [0],  # Robot 0
    [0],  # Robot 1
    [0],  # Robot 2
    [0]   # Robot 3
]

# Calculate the Euclidean distance between two points for the given coordinates
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Checking requirements
def check_requirements():
    # [Requirement 3] and [Requirement 5]
    total_demand_met = 0
    for tour in tours:
        load = 0
        for i in range(len(tour) - 1):
            load += demands[tour[i+1]]
            if load > 6000:
                return "FAIL"

        # As all tours contain only the depot, no goods are delivered at all.
        if len(tour) > 1:
            total_demand_met += load

    # [Requirement 1] All cities excluding depot must have been visited and returned to depot
    all_cities_delivered = set()
    for tour in tours:
        if tour[-1] != 0 or tour[0] != 0:  # must start and end at depot
            return "FAIL"
        for city in tour[1:-1]:
            all_cities_delivered.add(city)

    if len(all_cities_delivered) != 21:  # There are 21 cities excluding the depot
        return "FAIL"

    # [Requirement 4] Minimize travel costs. This check would need actual quantification to validate optimization, not feasible in simple unit test.
    
    # The output requirements checking:
    # [Requirement 6] & [Requirement 7] - Starts and ends at the depot, and total costs are outputted but not necessarily minimized
    for tour in tours:
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(tour[i], tour[i+1])
        if total_cost != 0:
            return "FAIL"

    return "CORRECT"

# Run the check
print(check_requirements())