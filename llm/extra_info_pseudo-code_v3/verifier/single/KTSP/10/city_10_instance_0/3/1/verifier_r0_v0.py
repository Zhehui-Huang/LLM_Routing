import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def evaluate_solution(tour, cities):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Does not start or end at depot city (city 0)
    
    if len(tour) != 5:  # 4 cities including depot + repeat of depot
        return "FAIL"  # Does not include exactly 4 cities with depot included
    
    visited_cities = set(tour)
    if 0 not in visited_cities or len(visited_cities) != 5:
        return "FAIL"  # Tour must have unique cities and exactly 4 different ones
    
    total_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        distance = calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])
        total_distance += distance
    
    # Assuming 'solution_distance' is the reported travel cost from the solution
    # if abs(total_distance - solution_distance) > 1e-5:
    #     return "FAIL"  # Correctness in travel cost calculation with small rounding tolerance
    
    # If all checks pass, solution might be considered correct
    return "CORRECT"

# Example check: Define cities with coordinates including the initial depot city
cities_coordinates = {
    0: (50, 42),  # Depot
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Define a hypothetical solution tour, should be tested for correctness
hypothetical_solution_tour = [0, 1, 2, 3, 0]  # Example tour
# hypothetical_solution_distance = 100  # Example reported total travel cost

# Now we would test the function using this setup.
print(evaluate_solution(hypothetical_solution_tour, cities_coordinates))