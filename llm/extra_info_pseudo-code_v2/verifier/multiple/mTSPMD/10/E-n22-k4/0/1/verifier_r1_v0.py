import math

# Sample data for cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Test solution provided
test_tour = [10, 6, 8, 11, 4, 3, 1, 2, 5, 7, 9, 12, 15, 18, 20, 17, 21, 19, 13, 16, 14, 0, 10]
reported_cost = 285.83

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def test_requirement_1(tour):
    # Assuming the depots are 0, 1, 2, 3 as per problem description
    return tour[0] == tour[-1] and tour[0] in [0, 1, 2, 3]

def test_requirement_2(tour):
    unique_cities = set(tour)
    return len(unique_cities) == len(cities) and all(city in unique_cities for city in cities)

def test_requirement_3(tour):
    test_cost = 0
    for i in range(len(tour) - 1):
        test_cost += calculate_distance(tour[i], tour[i + 1])
    return abs(test_cost - reported_cost) <= 1.0   # Allowing a small margin for floating-point precision issues

def test_requirement_5(tour):
    # Since all cities are visited, checking if length of tour minus two equals count of cities
    return len(tour) - 1 == len(cities) and tour[0] == tour[-1]

def perform_tests():
    results = []
    results.append(test_requirement_1(test_tour))
    results.append(test_requirement_2(test_tour))
    results.append(test_requirement_3(test_tour))
    results.append(test_requirement_5(test_tour))

    if all(results):
        print("CORRECT")
    else:
        print("FAIL")

perform_tests()