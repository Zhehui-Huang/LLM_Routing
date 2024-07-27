import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def verify_solution(tour, total_cost):
    # Define city coordinates
    cities = [
        (29, 51),  # Depot city 0
        (49, 20),  # City 1
        (79, 69),  # City 2
        (17, 20),  # City 3
        (18, 61),  # City 4
        (40, 57),  # City 5
        (57, 30),  # City 6
        (36, 12),  # City 7
        (93, 43),  # City 8
        (17, 36),  # City 9
        (4, 60),   # City 10
        (78, 82),  # City 11
        (83, 96),  # City 12
        (60, 50),  # City 13
        (98, 1)    # City 14
    ]

    # Groups containing city indices
    groups = [
        [1, 2, 5, 6],
        [8, 9, 10, 13],
        [3, 4, 7],
        [11, 12, 14]
    ]

    # Tour must start and end at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the actual travel cost in the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check calculated cost against supplied cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # Extract visited cities excluding depot
    visited_cities = tour[1:-1]
    
    # Check if exactly one city from each group is visited
    found_groups = [0 for _ in groups]
    for city in visited_cities:
        for i, group in enumerate(groups):
            if city in group:
                found_groups[i] += 1
    
    if any(count != 1 for count in found_groups):
        return "FAIL"

    return "CORRECT"

# Provided solution to test
tour_provided = [0, 5, 10, 4, 11, 0]
total_cost_provided = 184.24203302868492

# Running the verification
result = verify_solution(tour_provided, total_cost_provided)
print(result)