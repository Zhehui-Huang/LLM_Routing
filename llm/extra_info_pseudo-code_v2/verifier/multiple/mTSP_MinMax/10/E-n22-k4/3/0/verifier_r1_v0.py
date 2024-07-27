import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tours, costs, max_cost):
    # Coordinates for the cities including the depot city
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
        (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
        (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
        (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]

    # Requirement 1 & 2 check: Collectively visit all cities exactly once, return to depot
    all_cities_visited = set()
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        for city in tour[1:-1]:
            if city in all_cities_visited:
                return "FAIL"
            all_cities_visited.add(city)

    if len(all_cities_visited) != 21:  # As there are 21 cities excluding the depot
        return "FAIL"

    # Requirement 3 check: Minimize the maximum distance traveled
    computed_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        computed_costs.append(cost)
    
    if max(computed_costs) != max_cost:
        return "FAIL"

    # Requirement 5 check: Correctly reported costs
    if not all((abs(cost - actual_cost) < 1e-5 for cost, actual_cost in zip(computed_costs, costs))):
        return "FAIL"
    
    return "CORRECT"

# Solution provided
tours = [
    [0, 14, 17, 20, 10, 5, 4, 0],
    [0, 16, 19, 21, 9, 2, 0],
    [0, 12, 15, 18, 7, 1, 0],
    [0, 13, 11, 8, 6, 3, 0]
]
costs = [
    178.22357880921848,
    175.35845119802082,
    160.84575743680463,
    116.92108780425411
]
max_cost = 178.22786572156975  # There is slight issue with the provided max cost, should re-calculate or assert with a threshold

result = verify_solution(tours, costs, max_cost)
print(result)