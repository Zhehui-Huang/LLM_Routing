import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def test_solution():
    # Defining cities and coordinates
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
        (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
        (164, 193), (129, 189), (155, 185), (139, 182)
    ]
    
    # Solution provided
    tours = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    ]
    
    # Each robot starts from the depot 0
    for tour in tours:
        if tour[0] != 0:
            return "FAIL"

    # All cities from 0 to 21 should be visited exactly once
    all_visited_cities = set()
    for tour in tours:
        for city in tour:
            if city in all_visited_cities and city != 0:  # allowing depots to repeat as starting/ending nodes
                return "FAIL"
            all_visited_cities.add(city)
    
    if not all_visited_cities == set(range(22)):
        return "FAIL"
    
    # Validate each robot completes its tour at any node (not necessarily a depot)
    # This check is covered by allowed sequence of final node in each tour

    # Calculate the total distance should be non-negative and should be correctly calculated from coordinates
    overall_distance = 0
    for tour in tours:
        for i in range(len(tour) - 1):
            start = tour[i]
            end = tour[i + 1]
            overall_distance += calculate_distance(coordinates[start], coordinates[end])

    # Distance checks
    provided_costs = [0, 0, 0, 281.224]  # Implicit expected tour costs (assuming a correct computation on your side)
    computed_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            start = tour[i]
            end = tour[i + 1]
            cost += calculate_distance(coordinates[start], coordinates[end])
        computed_costs.append(cost)
        
    if not all(abs(pc - cc) < 1e-3 for pc, cc in zip(provided_costs, computed_costs)):
        return "FAIL"
    
    if overall_distance != sum(provided_costs):
        return "FAIL"
    
    return "CORRECT"

# Testing the given solution
print(test_solution())